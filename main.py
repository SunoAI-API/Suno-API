# -*- coding:utf-8 -*-

import os
import json

from fastapi import Depends, FastAPI, HTTPException, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security.api_key import APIKeyHeader

import schemas
from deps import get_token
from utils import complete_generation, generate_lyrics, generate_music, get_feed, get_lyrics, get_credits

API_KEY = os.getenv("API_KEY")
API_KEY_NAME = "X-API-Key"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

app = FastAPI(docs_url=None)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

async def get_api_key(api_key_header: str = Depends(api_key_header)):
    if api_key_header == API_KEY:
        return api_key_header
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Could not validate credentials"
        )


@app.get("/")
async def get_root(api_key: str = Depends(get_api_key)):
    return schemas.Response()


@app.post("/generate")
async def generate(
    data: schemas.CustomModeGenerateParam, token: str = Depends(get_token), api_key: str = Depends(get_api_key)
):
    try:
        resp = await generate_music(data.dict(), token)
        return resp
    except Exception as e:
        raise HTTPException(
            detail=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@app.post("/generate/description-mode")
async def generate_with_song_description(
    data: schemas.DescriptionModeGenerateParam, token: str = Depends(get_token), api_key: str = Depends(get_api_key)
):
    try:
        resp = await generate_music(data.dict(), token)
        return resp
    except Exception as e:
        raise HTTPException(
            detail=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@app.get("/feed/{aid}")
async def fetch_feed(aid: str, token: str = Depends(get_token), api_key: str = Depends(get_api_key)):
    try:
        resp = await get_feed(aid, token)
        return resp
    except Exception as e:
        raise HTTPException(
            detail=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@app.post("/generate/lyrics/")
async def generate_lyrics_post(request: Request, token: str = Depends(get_token), api_key: str = Depends(get_api_key)):
    req = await request.json()
    prompt = req.get("prompt")
    if prompt is None:
        raise HTTPException(
            detail="prompt is required", status_code=status.HTTP_400_BAD_REQUEST
        )

    try:
        resp = await generate_lyrics(prompt, token)
        return resp
    except Exception as e:
        raise HTTPException(
            detail=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    
@app.post("/generate/complete")
async def generate_complete(request: Request, token: str = Depends(get_token), api_key: str = Depends(get_api_key)):
    req = await request.json()
    clip_id = req.get("clip_id")
    if clip_id is None:
        raise HTTPException(
            detail="clip_id is required", status_code=status.HTTP_400_BAD_REQUEST
        )
    
    try:
        resp = await complete_generation(clip_id, token)
        return resp
    except Exception as e:
        raise HTTPException(
            detail=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@app.get("/lyrics/{lid}")
async def fetch_lyrics(lid: str, token: str = Depends(get_token), api_key: str = Depends(get_api_key)):
    try:
        resp = await get_lyrics(lid, token)
        return resp
    except Exception as e:
        raise HTTPException(
            detail=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@app.get("/get_credits")
async def fetch_credits(token: str = Depends(get_token), api_key: str = Depends(get_api_key)):
    try:
        resp = await get_credits(token)
        return resp
    except Exception as e:
        raise HTTPException(
            detail=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )