CC=gcc
CFLAGS=-Wall -I/usr/include/openssl
LDFLAGS=-lssl -lcrypto

all: generate_certs server client

generate_certs:
	chmod +x generate-certs.sh
	./generate-certs.sh

server:
	go build -o server server.go

client: client_cert.h
	$(CC) $(CFLAGS) -o client client.c $(LDFLAGS)

clean:
	rm -f server client *.key *.crt *.pem client_cert.h
