#!/usr/bin/env python3
""" Module to define BasicAuth
"""
from api.v1.auth.auth import Auth
from typing import TypeVar
import base64
from models.user import User


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

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """ Extract User credientials from decoded auth header
        """
        if decoded_base64_authorization_header is None or \
                type(decoded_base64_authorization_header) != str:
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        usr, pwd = decoded_base64_authorization_header.split(':', 1)
        return usr, pwd

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """ Create User object from credentials
        """
        if user_email is None or type(user_email) != str:
            return None
        if user_pwd is None or type(user_pwd) != str:
            return None

        try:
            email_match = User.search({'email': user_email})
        except Exception:
            return None

        for user in email_match:
            if user.is_valid_password(user_pwd):
                return user
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Return current User
        """
        auth_header = self.authorization_header(request)
        b64header = self.extract_base64_authorization_header(auth_header)
        credentials = self.decode_base64_authorization_header(b64header)
        email, pwd = self.extract_user_credentials(credentials)
        usr = self.user_object_from_credentials(email, pwd)
        return usr
