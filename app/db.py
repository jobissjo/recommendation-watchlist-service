from tortoise.contrib.sanic import register_tortoise
from sanic import Sanic
from app.config import settings

def init_db(app: Sanic):
    register_tortoise(
        app,
        db_url=settings.DATABASE_URL,
        modules={"models": ["app.models.watchlist"]},
        generate_schemas=True,
    )
