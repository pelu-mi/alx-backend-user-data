#!/usr/bin/env python3
""" Module to implement UserSession
"""
from models.base import Base


class UserSession(Base):
    """ Implement User Session storage model by storing session ids in db
    """
    def __init__(self, *args: list, **kwargs: dict):
        """ Initialization
        """
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
