#!/usr/bin/env python3
""" Module to test encryption using bcrypt
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """ Return a hashed password
    """
    return bcrypt.hashpw(bytes(password, 'utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Checks if hashed password is a valid encryption of password
    """
    return bcrypt.checkpw(bytes(password, 'utf-8'), hashed_password)
