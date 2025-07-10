from sanic import Blueprint
from sanic.response import json

watchlist_bp = Blueprint("Watchlist", url_prefix="/api/v1/watchlist")

@watchlist_bp.get("/")
async def get_watchlist(request):
    return json({"message": "Watch list V1 ✅"})
