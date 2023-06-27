#!/usr/bin/env python3
""" Integration testing for the project
"""
import requests


url = 'http://127.0.0.1:5000'


def register_user(email: str, password: str) -> None:
    """ Test user registration with email and password
    """
    r = requests.post('{}/users'.format(url),
                      data={'email': email, 'password': password})
    if r.status_code == 200:
        assert(r.json() == {"email": email, "message": "user created"})
    else:
        assert(r.status_code == 400)
        assert(r.json() == {"message": "email already registered"})


def log_in_wrong_password(email: str, password: str) -> None:
    """ Test login with wrong password
    """
    r = requests.post('{}/sessions'.format(url),
                      data={'email': email, 'password': password})
    assert r.status_code == 401


def log_in(email: str, password: str) -> str:
    """ Test login with correct password
    """
    r = requests.post('{}/sessions'.format(url),
                      data={'email': email, 'password': password})
    assert r.status_code == 200
    assert r.json() == {"email": email, "message": "logged in"}
    return r.cookies.get('session_id')


def profile_unlogged() -> None:
    """ Test profile page without logging in
    """
    r = requests.get('{}/profile'.format(url))
    assert r.status_code == 403


def profile_logged(session_id: str) -> None:
    """ Test profile page after logging in
    """
    r = requests.post('{}/profile'.format(url),
                      cookies={'session_id': session_id})
    # print(r.status_code)
    assert r.status_code == 200


def log_out(session_id: str) -> None:
    """ Test logging out
    """
    r = requests.delete('{}/sessions'.format(url),
                      cookies={'session_id': session_id})
    if r.status_code == 302:
        assert r.url == 'http://127.0.0.1:5000/'
    else:
        assert r.status_code == 200


def reset_password_token(email: str) -> str:
    """ Test password reset
    """
    r = requests.post('{}/reset_password'.format(url),
                      data={'email': email})
    if r.status_code == 200:
        return r.json().get('reset_token')
    assert r.status_code == 401


def update_password(email: str, reset_token: str,
                    new_password: str) -> None:
    """ Test password update using reset_token
    """
    data = {
        'email': email,
        'reset_token': reset_token,
        'new_password': new_password,
    }
    r = requests.put('{}/reset_password'.format(url),
                     data=data)
    if r.status_code == 200:
        assert r.json() == {"email": email, "message": "Password updated"}
    else:
        assert r.status_code == 403


# Template code from task here

EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
