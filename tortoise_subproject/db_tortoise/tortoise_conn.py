import asyncio
import os

from tortoise import connections, Tortoise
from dotenv import load_dotenv

load_dotenv()


async def init_db():
    await Tortoise.init(
        {
            "connections": {
                "default": {
                    "engine": "tortoise.backends.asyncpg",
                    "credentials": {
                        "host": os.environ["TT_HOST"],
                        "port": os.environ["TT_PORT"],
                        "user": os.environ["TT_USER"],
                        "password": os.environ["TT_PASS"],
                        "database": os.environ["TT_DB"],
                    },
                }
            },
            "apps": {
                "models": {
                    "models": ["tortoise_subproject.models.models"],
                    "default_connection": "default"}},
        }
    )


asyncio.run(init_db())
