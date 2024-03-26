# -*- coding:utf-8 -*-

from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.middleware.cors import CORSMiddleware
from utils import generate_music, get_feed
from deps import get_token

import schemas

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def get_root():
    return schemas.Response


@app.post("/generate")
async def generate(data: schemas.GenerateBase, token: str = Depends(get_token)):
    try:
        resp = await generate_music(data, token)
        return resp.json()
    except Exception as e:
        raise HTTPException(detail=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@app.get("/feed/{aid}")
async def fetch_feed(aid: str, token: str = Depends(get_token)):
    print(token)
    try:
        resp = await get_feed(aid, token)
        return resp.json()
    except Exception as e:
        raise HTTPException(detail=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
