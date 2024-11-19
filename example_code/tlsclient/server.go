package main

import (
	"crypto/tls"
	"crypto/x509"
	"flag"
	"fmt"
	"io"
	"log"
	"net"
	"os"
)

func main() {
	// Parse command line arguments
	addr := flag.String("addr", "localhost", "bind address")
	port := flag.Int("port", 8443, "bind port")
	caCert := flag.String("ca", "ca.crt", "CA certificate file")
	serverCert := flag.String("cert", "server.crt", "server certificate file")
	serverKey := flag.String("key", "server.key", "server private key file")
	flag.Parse()

	// Load CA certificate
	caPEM, err := os.ReadFile(*caCert)
	if err != nil {
		log.Fatalf("Failed to read CA certificate: %v", err)
	}
	caPool := x509.NewCertPool()
	if !caPool.AppendCertsFromPEM(caPEM) {
		log.Fatal("Failed to parse CA certificate")
	}

	// Configure TLS
	cert, err := tls.LoadX509KeyPair(*serverCert, *serverKey)
	if err != nil {
		log.Fatalf("Failed to load server certificate and key: %v", err)
	}

	config := &tls.Config{
		Certificates: []tls.Certificate{cert},
		ClientCAs:    caPool,
		ClientAuth:   tls.RequireAndVerifyClientCert,
	}

	// Create listener
	listener, err := tls.Listen("tcp", fmt.Sprintf("%s:%d", *addr, *port), config)
	if err != nil {
		log.Fatalf("Failed to create listener: %v", err)
	}
	defer listener.Close()

	log.Printf("Server listening on %s:%d", *addr, *port)

	for {
		conn, err := listener.Accept()
		if err != nil {
			log.Printf("Failed to accept connection: %v", err)
			continue
		}
		go handleConnection(conn)
	}
}

func handleConnection(conn net.Conn) {
	defer conn.Close()

	tlsConn := conn.(*tls.Conn)
	if err := tlsConn.Handshake(); err != nil {
		log.Printf("TLS handshake failed: %v", err)
		return
	}

	buffer := make([]byte, 1024)
	for {
		n, err := conn.Read(buffer)
		if err != nil {
			if err != io.EOF {
				log.Printf("Read error: %v", err)
			}
			return
		}

		_, err = conn.Write(buffer[:n])
		if err != nil {
			log.Printf("Write error: %v", err)
			return
		}
	}
}
