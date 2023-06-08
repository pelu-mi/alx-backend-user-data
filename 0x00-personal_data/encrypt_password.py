#!/usr/bin/env python3
""" Module to test encryption using bcrypt
"""

import bcrypt


def hash_password(password: str) -> str:
    """ Return a hashed password
    """
    return bcrypt.hashpw(bytes(password, 'utf-8'), bcrypt.gensalt())
