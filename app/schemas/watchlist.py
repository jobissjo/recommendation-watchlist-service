from pydantic import BaseModel
from uuid import UUID
from typing import Optional, TypeVar, Generic
from app.schemas.common import BaseResponseSchema

T = TypeVar("T", bound=BaseModel)


class WatchListItemSchema(BaseModel):
    title: str
    type: str
    is_recommended: bool
    instance_id: Optional[UUID]




class WatchListResponseSchema(BaseResponseSchema):
    data: list[WatchListItemSchema]


class ErrorResponseSchema(BaseModel):
    success: bool = False
    message: str
    error: Optional[str] = None