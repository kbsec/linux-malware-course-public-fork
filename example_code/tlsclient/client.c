#include "client_cert.h"
#include <arpa/inet.h>  // for inet_pton
#include <netinet/in.h> // for struct sockaddr_in
#include <openssl/err.h>
#include <openssl/ssl.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h> // for AF_INET, SOCK_STREAM
#include <unistd.h>

void handle_error(const char *msg) {
  fprintf(stderr, "%s\n", msg);
  ERR_print_errors_fp(stderr);
  exit(1);
}

int main(int argc, char *argv[]) {
  if (argc != 3) {
    fprintf(stderr, "Usage: %s <host> <port>\n", argv[0]);
    exit(1);
  }

  const char *host = argv[1];
  int port = atoi(argv[2]);

  // Initialize OpenSSL
  SSL_library_init();
  OpenSSL_add_all_algorithms();
  SSL_load_error_strings();

  // Create SSL context
  SSL_CTX *ctx = SSL_CTX_new(TLS_client_method());
  if (!ctx) {
    handle_error("Failed to create SSL context");
  }

  // Load embedded client certificate and private key
  BIO *bio = BIO_new_mem_buf(client_pem, client_pem_len);
  X509 *cert = PEM_read_bio_X509(bio, NULL, 0, NULL);
  BIO_reset(bio);
  EVP_PKEY *key = PEM_read_bio_PrivateKey(bio, NULL, 0, NULL);
  BIO_free(bio);

  if (!SSL_CTX_use_certificate(ctx, cert) ||
      !SSL_CTX_use_PrivateKey(ctx, key)) {
    handle_error("Failed to load certificate and private key");
  }

  // Create socket and connect
  int sock = socket(AF_INET, SOCK_STREAM, 0);
  if (sock < 0) {
    handle_error("Failed to create socket");
  }

  struct sockaddr_in addr;
  memset(&addr, 0, sizeof(addr));
  addr.sin_family = AF_INET;
  addr.sin_port = htons(port);
  if (inet_pton(AF_INET, host, &addr.sin_addr) != 1) {
    handle_error("Invalid address");
  }

  if (connect(sock, (struct sockaddr *)&addr, sizeof(addr)) != 0) {
    handle_error("Failed to connect");
  }

  // Create SSL connection
  SSL *ssl = SSL_new(ctx);
  SSL_set_fd(ssl, sock);

  if (SSL_connect(ssl) != 1) {
    handle_error("SSL connection failed");
  }

  // Send 10 pings
  char buf[1024];
  for (int i = 0; i < 10; i++) {
    const char *msg = "ping\n";
    if (SSL_write(ssl, msg, strlen(msg)) <= 0) {
      handle_error("Failed to write");
    }

    int len = SSL_read(ssl, buf, sizeof(buf) - 1);
    if (len <= 0) {
      handle_error("Failed to read");
    }
    buf[len] = '\0';
    printf("Received: %s", buf);

    sleep(1);
  }

  // Cleanup
  SSL_shutdown(ssl);
  SSL_free(ssl);
  close(sock);
  SSL_CTX_free(ctx);
  X509_free(cert);
  EVP_PKEY_free(key);
  ERR_free_strings();

  return 0;
}
