from sanic.request import Request
from app.utils.jwt_utils import verify_jwt_token
from sanic.exceptions import Unauthorized

async def authenticate_request(request: Request):
    if request.path.startswith("/protected"):
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            raise Unauthorized("Missing or invalid Authorization header")
        
        token = auth_header.split(" ")[1]
        payload = verify_jwt_token(token)
        request.ctx.user = payload
