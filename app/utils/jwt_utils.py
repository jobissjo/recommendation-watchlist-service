from jose import jwt, JWTError, ExpiredSignatureError
from sanic.exceptions import Unauthorized
from app.config import settings

def verify_jwt_token(token: str):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        if payload.get("token_type") != "access":
            raise Unauthorized("Invalid token type")
        return payload
    except ExpiredSignatureError:
        raise Unauthorized("Token expired")
    except JWTError:
        raise Unauthorized("Invalid token")
