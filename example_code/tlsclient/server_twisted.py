#!/usr/bin/env python3

from twisted.internet import ssl, reactor, protocol
from twisted.python import log
from twisted.internet.endpoints import SSL4ServerEndpoint
from OpenSSL import SSL
import sys
import argparse

class EchoProtocol(protocol.Protocol):
    def connectionMade(self):
        peer = self.transport.getPeer()
        log.msg(f"New connection from {peer.host}:{peer.port}")

    def dataReceived(self, data):
        # Echo back the received data
        self.transport.write(data)

    def connectionLost(self, reason):
        peer = self.transport.getPeer()
        log.msg(f"Connection lost from {peer.host}:{peer.port}: {reason.getErrorMessage()}")


class EchoFactory(protocol.Factory):
    protocol = EchoProtocol


def verify_client_cert(conn, x509, errno, errdepth, ok):
    """
    Custom certificate verification callback.
    This gets called for each certificate in the chain.
    """
    if not ok:
        common_name = x509.get_subject().commonName
        log.msg(f"Invalid certificate from {common_name}")
        return False
    
    # Certificate is valid
    if errdepth == 0:  # This is the leaf certificate
        common_name = x509.get_subject().commonName
        log.msg(f"Valid client certificate from {common_name}")
    return True


def create_context_factory(ca_cert, server_cert, server_key):
    """Create SSL context factory with client verification."""
    
    class ServerContextFactory(ssl.ContextFactory):
        def getContext(self):
            ctx = SSL.Context(SSL.TLS_METHOD)
            
            # Load server certificate and private key
            ctx.use_certificate_file(server_cert)
            ctx.use_privatekey_file(server_key)
            ctx.check_privatekey()  # Verify private key matches certificate
            
            # Load CA certificate and require client certs
            ctx.load_verify_locations(ca_cert)
            ctx.set_verify(
                SSL.VERIFY_PEER | SSL.VERIFY_FAIL_IF_NO_PEER_CERT,
                verify_client_cert
            )
            
            return ctx
    
    return ServerContextFactory()


def main():
    parser = argparse.ArgumentParser(description='Twisted TLS Echo Server with Client Certificate Verification')
    parser.add_argument('--addr', default='localhost', help='bind address')
    parser.add_argument('--port', type=int, default=8443, help='bind port')
    parser.add_argument('--ca', default='ca.crt', help='CA certificate file')
    parser.add_argument('--cert', default='server.crt', help='server certificate file')
    parser.add_argument('--key', default='server.key', help='server private key file')
    
    args = parser.parse_args()

    # Set up logging
    log.startLogging(sys.stdout)

    # Create SSL context factory
    context_factory = create_context_factory(
        args.ca,
        args.cert,
        args.key
    )

    # Create endpoint
    endpoint = SSL4ServerEndpoint(
        reactor,
        args.port,
        context_factory,
        interface=args.addr
    )

    # Set up the server
    d = endpoint.listen(EchoFactory())
    
    def listen_success(port):
        log.msg(f"Server listening on {args.addr}:{args.port}")
    
    def listen_failure(failure):
        log.err(f"Could not bind to port: {failure.getErrorMessage()}")
        reactor.stop()
    
    d.addCallbacks(listen_success, listen_failure)

    # Run the server
    reactor.run()


if __name__ == '__main__':
    main()
