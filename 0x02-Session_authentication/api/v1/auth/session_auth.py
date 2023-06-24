#!/usr/bin/env python3
""" Module for Session Auth implementation
"""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """ Session Auth implementation
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ Create session id for a user
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        sess_id = str(uuid.uuid4())
        self.user_id_by_session_id[sess_id] = user_id
        return sess_id
