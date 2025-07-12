from app.repositories import WatchlistRepository
from app.models import WatchItem
from tortoise.contrib.pydantic import pydantic_model_creator

WatchItemPydantic = pydantic_model_creator(WatchItem, name="WatchItem")

class WatchlistService:
    @staticmethod
    async def get_watchlist(user_id: str):
        items = await WatchlistRepository.get_watchlist(user_id)
        serialized_items = []
        for item in items:
            pydantic_item = await WatchItemPydantic.from_tortoise_orm(item)
            serialized_items.append(pydantic_item.model_dump())
        return serialized_items
    
    @staticmethod
    async def create_watchlist_item(data: dict):
        return await WatchlistRepository.create_watchlist_item(data)
    
    @staticmethod
    async def get_watchlist_item(item_id: str):
        item = await WatchlistRepository.get_watchlist_item(item_id)
        pydantic_item = await WatchItemPydantic.from_tortoise_orm(item)
        return pydantic_item.model_dump()
    
    @staticmethod
    async def update_watchlist_item(item_id: str, data: dict):
        return await WatchlistRepository.update_watchlist_item(item_id, data)
    
    @staticmethod
    async def delete_watchlist_item(item_id: str):
        return await WatchlistRepository.delete_watchlist_item(item_id)
