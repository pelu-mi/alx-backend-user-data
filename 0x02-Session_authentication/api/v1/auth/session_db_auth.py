#!/usr/bin/env python3
""" Module for Session DB Auth
"""
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession
from datetime import datetime, timedelta


class SessionDBAuth(SessionExpAuth):
    """ SessionDBAuth implementation
    """
    def create_session(self, user_id=None):
        """ Create session
        """
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        user = UserSession()
        user.user_id = user_id
        user.session_id = session_id
        user.save()
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """ Get user id based on session id
        """
        if session_id is None:
            return None

        UserSession.load_from_file()
        sessions = UserSession.search({'session_id': session_id})
        if not sessions:
            return None
        session = sessions[0]

        expired_at = session.created_at + \
            timedelta(seconds=self.session_duration)
        if expired_at < datetime.now():
            return None

        return session.user_id

    def destroy_session(self, request=None):
        """ Destroy the session
        """
        '''
        destroyed = super().destroy_session(request)
        if destroyed:
            session_id = request.cookies.get('session_id')
            user = UserSession.search({'session_id': session_id})
            if not user:
                return False
            user[0].remove()
            return True
        '''
        session_id = self.session_cookie(request)
        try:
            sessions = UserSession.search({'session_id': session_id})
        except Exception:
            return False
        if len(sessions) <= 0:
            return False
        sessions[0].remove()
        return True
