import asyncio

import uvicorn
from fastapi import FastAPI

from routers.v1.ml.scientific_test import router as scientific_test_router
from routers.v1.ml.personality_test import router as personality_test_router
from routers.v1.ml.summarize import router as summarize_router
from settings import settings


app = FastAPI()

app.include_router(scientific_test_router, prefix="/scientific_test", tags=["Scientific test"])
app.include_router(personality_test_router, prefix="/personality_test", tags=["MBTI test"])
app.include_router(summarize_router, prefix="/summarize", tags=["Summarize"])


async def main():
    uvicorn.run("main:app",
                host=settings.ADDR,
                port=settings.PORT,
                reload=settings.TEST,
                log_level=settings.LOG_LEVEL)


if __name__ == "__main__":
    asyncio.run(main())
