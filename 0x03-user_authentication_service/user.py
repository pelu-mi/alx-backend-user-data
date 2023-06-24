#!/usr/bin/env python3
""" Module for User Model
"""
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    """ User model for table 'users'
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(VARCHAR(250), nullable=False)
    hashed_password = Column(VARCHAR(250), nullable=False)
    session_id = Column(VARCHAR(250))
    reset_token = Column(VARCHAR(250))
