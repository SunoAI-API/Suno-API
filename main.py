# -*- coding:utf-8 -*-
import datetime
import logging
import os

import sqlalchemy
from fastapi import FastAPI, HTTPException, Request, status
from fastapi.middleware.cors import CORSMiddleware

import schemas
from cookie import cookie_from_auth_session
from db import Base, AuthSession
from utils import generate_lyrics, generate_music, get_feed, get_lyrics, get_credits

from sqlalchemy import create_engine
from sqlalchemy import select
from sqlalchemy.orm import sessionmaker

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

engine = create_engine(os.getenv("DATABASE_URL", "sqlite:///db.sqlite"), echo=False)
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)


def get_cookie(session_id: int = None):
    with (Session.begin() as session):
        stmt = select(AuthSession).order_by(AuthSession.last_usage).where(AuthSession.is_disabled == 0).limit(1).with_for_update()

        if session_id:
            stmt = stmt.where(AuthSession.id == session_id)

        try:
            auth_session = session.scalars(stmt).one()
        except sqlalchemy.exc.NoResultFound:
            raise RuntimeError("No sessions available")

        auth_session.last_usage = datetime.datetime.now()

        cookie = cookie_from_auth_session(auth_session)

        try:
            cookie.update_token()
        except RuntimeError as e:
            if str(e) == "signed_out":
                auth_session.is_disabled = 1
                session.commit()

                if session_id is None:
                    return get_cookie()

                raise RuntimeError("Session is invalid")

        session.commit()

    return cookie

@app.get("/")
async def get_root():
    return schemas.Response()


@app.post("/generate")
async def generate(
        data: schemas.CustomModeGenerateParam
):
    try:
        cookie = get_cookie(data.dict().get('session_id'))
        resp = await generate_music(data.dict(), cookie.get_token(), cookie.get_proxy())
        resp["session_id"] = cookie.get_auth_session_id()
        return resp
    except Exception as e:
        logging.error(e)
        raise HTTPException(
            detail=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@app.post("/generate/description-mode")
async def generate_with_song_description(
        data: schemas.DescriptionModeGenerateParam
):
    try:
        cookie = get_cookie(data.dict().get('session_id'))
        resp = await generate_music(data.dict(), cookie.get_token(), cookie.get_proxy())
        resp["session_id"] = cookie.get_auth_session_id()
        return resp
    except Exception as e:
        logging.error(e)
        raise HTTPException(
            detail=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@app.get("/feed/{aid}")
async def fetch_feed(aid: str, session_id: int):
    try:
        cookie = get_cookie(session_id)
        resp = await get_feed(aid, cookie.get_token(), cookie.get_proxy())
        return resp
    except Exception as e:
        logging.error(e)
        raise HTTPException(
            detail=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@app.post("/generate/lyrics")
async def generate_lyrics_post(request: Request, session_id: int = None):
    req = await request.json()
    prompt = req.get("prompt")
    if prompt is None:
        raise HTTPException(
            detail="prompt is required", status_code=status.HTTP_400_BAD_REQUEST
        )

    try:
        cookie = get_cookie(session_id)
        resp = await generate_lyrics(prompt, cookie.get_token(), cookie.get_proxy())
        return resp
    except Exception as e:
        logging.error(e)
        raise HTTPException(
            detail=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@app.get("/lyrics")
async def fetch_lyrics(lid: str, session_id: int):
    try:
        cookie = get_cookie(session_id)
        resp = await get_lyrics(lid, cookie.get_token(), cookie.get_proxy())
        return resp
    except Exception as e:
        logging.error(e)
        raise HTTPException(
            detail=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@app.get("/get_credits")
async def fetch_credits(session_id: int):
    try:
        cookie = get_cookie(session_id)
        resp = await get_credits(cookie.get_token(), cookie.get_proxy())
        return resp
    except Exception as e:
        logging.error(e)
        raise HTTPException(
            detail=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
