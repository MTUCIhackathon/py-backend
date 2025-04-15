import asyncio
import logging

import uvicorn
from fastapi import FastAPI
from uvicorn import config

from routers.v1.ml.scientific_test import router as scientific_test_router
from routers.v1.ml.personality_test import router as personality_test_router
from routers.v1.ml.generate_ai_test import router as ai_test_router
from routers.v1.ml.summarize import router as summarize_router
from routers import router
from settings import settings

app = FastAPI()

logger = logging.getLogger(__name__)

app.include_router(router)

async def main():
    cfg = config.Config(
        "main:app",
        host=settings.ADDR,
        port=settings.PORT,
        reload=settings.TEST,
        log_level=settings.LOG_LEVEL
    )

    server = uvicorn.Server(cfg)

    await server.serve()


if __name__ == "__main__":
    asyncio.run(main())
