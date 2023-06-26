#!/usr/bin/env python3
""" Module for authentication implementation
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """ Create salted hash password
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
