#!/usr/bin/env python3
""" Module to define BasicAuth
"""
from api.v1.auth.auth import Auth


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
