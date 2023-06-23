#!/usr/bin/env python3
""" Module to define BasicAuth
"""
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """ Basic Authentication system
    """
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """ Extract base64 encoded string from the header
        """
        if authorization_header is None or type(authorization_header) != str:
            return None
        if not authorization_header.startswith('Basic '):
            return None
        return authorization_header.split()[1]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """ Decode base64 encoded string
        """
        if base64_authorization_header is None or \
                type(base64_authorization_header) != str:
            return None
        try:
            encoded_str = base64_authorization_header.encode('utf-8')
            decoded_str = base64.b64decode(encoded_str)
            return decoded_str.decode('utf-8')
        except Exception:
            return None
