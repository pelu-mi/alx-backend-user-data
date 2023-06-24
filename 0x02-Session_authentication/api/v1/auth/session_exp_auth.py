#!/usr/bin/env python3
""" Module to implement Session Auth with expiration time
"""
from api.v1.auth.session_auth import SessionAuth
from os import getenv
from datetime import datetime, timedelta


class SessionExpAuth(SessionAuth):
    """ SessionExpAuth implementation
    """
    def __init__(self):
        """ Initialization
        """
        duration = getenv('SESSION_DURATION')
        if not duration or not duration.isnumeric():
            self.session_duration = 0
        else:
            self.session_duration = int(duration)

    def create_session(self, user_id=None):
        """ Create session and save time of creation
        """
        session_id = super().create_session(user_id)
        if not session_id:
            return None
        self.user_id_by_session_id[session_id] = {
            'user_id': user_id,
            'created_at': datetime.now()
        }
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """ Get user id based on session_id
        """
        if session_id is None:
            return None
        if session_id not in self.user_id_by_session_id:
            return None

        session_dict = self.user_id_by_session_id.get(session_id)
        if self.session_duration <= 0:
            return session_dict.get('user_id')

        created_at = session_dict.get('created_at')
        if not created_at:
            return None
        expired_at = created_at + timedelta(seconds=self.session_duration)
        if expired_at < datetime.now():
            self.user_id_by_session_id.pop(session_id, None)
            return None
        return session_dict.get('user_id')
