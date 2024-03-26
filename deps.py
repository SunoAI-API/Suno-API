# -*- coding:utf-8 -*-

from cookie import suno_auth


def get_token():
    token = suno_auth.get_token()
    try:
        yield token
    finally:
        pass
