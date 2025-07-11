from sanic import Blueprint
from sanic.response import json
from sanic_ext import openapi
from app.schemas import  WatchListResponseSchema
from app.services import WatchlistService
from app.utils import APIResponse

watchlist_bp = Blueprint("Watchlist", url_prefix="/api/v1/watchlist")

@watchlist_bp.get("/")    
@openapi.definition(summary="Watch list V1", tag=['Watchlist'], response={200: WatchListResponseSchema})
async def get_watchlist(request):
    data = await WatchlistService.get_watchlist('3fa85f64-5717-4562-b3fc-2c963f66afa6')
    print(data, 'data', type(data))
    return await APIResponse.success(message='Watchlist retrieved successfully', data=data)
