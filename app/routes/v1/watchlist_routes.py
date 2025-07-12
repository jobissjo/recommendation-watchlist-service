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

@watchlist_bp.post("/")
async def create_watchlist_item(request):
    data = request.json
    item = await WatchlistService.create_watchlist_item(data)
    return await APIResponse.created(message='Watchlist item created successfully', data=item)


@watchlist_bp.get("/<item_id>")
async def get_watchlist_item(request, item_id):
    item = await WatchlistService.get_watchlist_item(item_id)
    return await APIResponse.success(message='Watchlist item retrieved successfully', data=item)

@watchlist_bp.put("/<item_id>")
async def update_watchlist_item(request, item_id):
    data = request.json
    item = await WatchlistService.update_watchlist_item(item_id, data)
    return await APIResponse.success(message='Watchlist item updated successfully', data=item)

@watchlist_bp.delete("/<item_id>")
async def delete_watchlist_item(request, item_id):
    item = await WatchlistService.delete_watchlist_item(item_id)
    return await APIResponse.success(message='Watchlist item deleted successfully', data=item)