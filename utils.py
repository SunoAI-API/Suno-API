import time

import os
import aiohttp
from dotenv import load_dotenv
load_dotenv()


BASE_URL = os.getenv("BASE_URL")


COMMON_HEADERS = {
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    "Referer": "https://app.suno.ai/",
    "Origin": "https://app.suno.ai",
}


async def fetch(url, headers=None, data=None):

    if headers is None:
        headers = {}
    headers.update(COMMON_HEADERS)

    async with aiohttp.ClientSession() as session:
        try:
            async with session.post(url=url, data=data, headers=headers) as resp:
                return await resp.text()
        except Exception as e:
            return f"An error occurred: {e}"


async def get_feed(ids, token):
    headers = {
        "Authorization": f"Bearer {token}"
    }
    api_url = f"{BASE_URL}/api/feed/?ids={ids}"
    response = await fetch(api_url, headers)
    return response


async def generate_music(data, token):
    headers = {
        "Authorization": f"Bearer {token}"
    }
    api_url = f"{BASE_URL}/api/generate/v2/"
    response = await fetch(api_url, headers, data)
    return response

