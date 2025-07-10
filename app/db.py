from tortoise.contrib.sanic import register_tortoise
from sanic import Sanic
from app.config import settings

def init_db(app: Sanic):
    register_tortoise(
        app,
        db_url=settings.DATABASE_URL or "sqlite://db.sqlite3",
        modules={"models": ["app.models.wathlist"]},
        generate_schemas=True,
    )
