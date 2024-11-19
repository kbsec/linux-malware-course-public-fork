#!/usr/bin/env python3

import socket
import ssl
import sys
import argparse
import threading
from typing import Tuple


def handle_client(conn: ssl.SSLSocket, addr: Tuple[str, int]) -> None:
    """Handle individual client connections."""
    try:
        # Perform explicit handshake
        conn.do_handshake()
        print(f"Secure connection established with {addr}")
        
        while True:
            data = conn.recv(1024)
            if not data:
                break
            # Echo the data back
            conn.send(data)
            
    except ssl.SSLError as e:
        print(f"SSL error occurred with {addr}: {e}")
    except Exception as e:
        print(f"Error handling client {addr}: {e}")
    finally:
        conn.close()
        print(f"Connection closed with {addr}")


def main():
    parser = argparse.ArgumentParser(description='TLS Echo Server with Client Certificate Verification')
    parser.add_argument('--addr', default='localhost', help='bind address')
    parser.add_argument('--port', type=int, default=8443, help='bind port')
    parser.add_argument('--ca', default='ca.crt', help='CA certificate file')
    parser.add_argument('--cert', default='server.crt', help='server certificate file')
    parser.add_argument('--key', default='server.key', help='server private key file')
    
    args = parser.parse_args()

    # Create SSL context
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    
    try:
        # Load server certificate and private key
        context.load_cert_chain(certfile=args.cert, keyfile=args.key)
        
        # Load CA certificate for client verification
        context.load_verify_locations(cafile=args.ca)
        
        # Require client certificate
        context.verify_mode = ssl.CERT_REQUIRED
        
        # Create and configure the socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        # Bind and listen
        sock.bind((args.addr, args.port))
        sock.listen(5)
        
        print(f"Server listening on {args.addr}:{args.port}")
        
        while True:
            # Accept connections
            client_sock, addr = sock.accept()
            print(f"Received connection from {addr}")
            
            try:
                # Wrap the socket with SSL/TLS
                ssl_conn = context.wrap_socket(
                    client_sock,
                    server_side=True,
                )
                
                # Handle client in a new thread
                client_thread = threading.Thread(
                    target=handle_client,
                    args=(ssl_conn, addr)
                )
                client_thread.start()
                
            except ssl.SSLError as e:
                print(f"SSL error during handshake with {addr}: {e}")
                client_sock.close()
            except Exception as e:
                print(f"Error handling connection from {addr}: {e}")
                client_sock.close()
                
    except Exception as e:
        print(f"Server error: {e}")
        sys.exit(1)
    finally:
        sock.close()


if __name__ == "__main__":
    main()
