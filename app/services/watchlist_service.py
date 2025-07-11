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
