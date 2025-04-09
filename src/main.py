import asyncio

import uvicorn
from fastapi import FastAPI

from routers import router
from settings import settings

app = FastAPI()
app.include_router(router=router)


async def main():
    uvicorn.run("main:app",
                host=settings.ADDR,
                port=settings.PORT,
                reload=settings.TEST,
                log_level=settings.LOG_LEVEL)


if __name__ == "__main__":
    asyncio.run(main())
