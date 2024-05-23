# -*- coding:utf-8 -*-

from http.cookies import SimpleCookie

import requests

from db import AuthSession
from utils import COMMON_HEADERS


def cookie_from_auth_session(session: AuthSession):
    cookie = SunoCookie()
    cookie.load_cookie(session.cookie)
    cookie.set_session_id(session.session_id)
    cookie.set_auth_session_id(session.id)

    if session.proxy:
        cookie.set_proxy(session.proxy.address)

    return cookie


class SunoCookie:
    def __init__(self):
        self.cookie = SimpleCookie()
        self.session_id = None
        self.token = None
        self.proxy = None
        self.auth_session_id = None

    def load_cookie(self, cookie_str):
        self.cookie.load(cookie_str)

    def get_cookie(self):
        return ";".join([f"{i}={self.cookie.get(i).value}" for i in self.cookie.keys()])

    def set_session_id(self, session_id):
        self.session_id = session_id

    def get_session_id(self):
        return self.session_id

    def get_token(self):
        return self.token

    def set_token(self, token: str):
        self.token = token

    def get_proxy(self):
        return self.proxy

    def set_proxy(self, proxy):
        self.proxy = proxy

    def set_auth_session_id(self, auth_session_id):
        self.auth_session_id = auth_session_id

    def get_auth_session_id(self):
        return self.auth_session_id

    def update_token(self):
        headers = {"cookie": self.get_cookie()}
        headers.update(COMMON_HEADERS)

        proxies = None
        if self.get_proxy():
            proxies = {
                'http': self.get_proxy(),
                'https': self.get_proxy()
            }

        resp = requests.post(
            url=f"https://clerk.suno.com/v1/client/sessions/{self.get_session_id()}/tokens?_clerk_js_version=4.72.0-snapshot.vc141245",
            headers=headers,
            proxies=proxies
        )

        if resp.status_code != 200:
            raise RuntimeError(resp.json()["errors"][0]["code"])

        resp_headers = dict(resp.headers)
        set_cookie = resp_headers.get("Set-Cookie")
        self.load_cookie(set_cookie)
        token = resp.json().get("jwt")
        self.set_token(token)
