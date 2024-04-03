# -*- coding:utf-8 -*-

from datetime import datetime
from typing import Any, List, Optional, Union

from pydantic import BaseModel, Field


class Response(BaseModel):
    code: Optional[int] = 0
    msg: Optional[str] = "success"
    data: Optional[Any] = None


class GenerateBase(BaseModel):
    """Generate with Custom Mode"""

    prompt: str
    mv: str
    title: str
    tags: str
    continue_at: Optional[str] = None
    continue_clip_id: Optional[str] = None




