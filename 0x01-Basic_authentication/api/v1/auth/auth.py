#!/usr/bin/env python3
""" Module for API Authentication
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ Authentication system template
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Determine if authentication is required
        """
        return False

    def authorization_header(self, request=None) -> str:
        """ Authorization header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Get the current user
        """
        return None
