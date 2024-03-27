import requests
import json


def test_generate_music():
    data = {
        "prompt": "[Verse]\nWake up in the morning, feeling brand new\nGonna shake off the worries, leave 'em in the rearview\nStep outside, feeling the warmth on my face\nThere's something 'bout the sunshine that puts me in my place\n\n[Verse 2]\nWalking down the street, got a spring in my step\nThe rhythm in my heart, it just won't forget\nEverywhere I go, people smiling at me\nThey can feel the joy, it's contagious, can't you see?\n\n[Chorus]\nI got sunshine in my pocket, happiness in my soul\nA skip in my stride, and I'm ready to go\nNothing gonna bring me down, gonna keep on shining bright\nI got sunshine in my pocket, this world feels so right",
        "tags": "heartfelt anime",
        "mv": "chirp-v3-0",
        "title": "Sunshine in your Pocket",
        "continue_clip_id": None,
        "continue_at": None
    }

    r = requests.post("http://127.0.0.1:8000/generate", data=json.dumps(data))

    resp = r.text
    print(resp)


def test_generate_lyrics():
    data = {
        "prompt":  ""
    }

    r = requests.post("http://127.0.0.1:8000/generate/lyrics/", data=json.dumps(data))
    print(r.text)


def get_lyrics(lid):
    r = requests.get(f"http://127.0.0.1:8000/lyrics/{lid}")
    print(r.text)
