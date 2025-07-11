from app.models import WatchItem


class WatchlistRepository:
    @staticmethod
    async def get_watchlist(user_id: str):
        return await WatchItem.filter(user_id=user_id)
    
    @staticmethod
    async def get_watchlist_item(item_id: str):
        return await WatchItem.get(id=item_id)
    
    @staticmethod
    async def create_watchlist_item(data: dict):
        return await WatchItem.create(**data)
    
    @staticmethod
    async def update_watchlist_item(item_id: str, data: dict):
        await WatchItem.filter(id=item_id).update(**data)
        return await WatchItem.get(id=item_id)
    
    @staticmethod
    async def delete_watchlist_item(item_id: str):
        return await WatchItem.filter(id=item_id).delete()
    

    @staticmethod
    async def get_recommended_items(user_id: str):
        return await WatchItem.filter(
            user_id=user_id, 
            is_recommended=True
        ).all()
    
