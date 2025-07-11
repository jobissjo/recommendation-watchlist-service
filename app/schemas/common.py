from pydantic import BaseModel

class BaseResponseSchema(BaseModel):
    success: bool = True
    message: str