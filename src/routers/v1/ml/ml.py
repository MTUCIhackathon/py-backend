from fastapi import APIRouter

from cores.errors import with_errors
from schemas.ml import Response

router = APIRouter()

@router.get("/ping",
            name="ping",
            responses=with_errors(),
            response_model=Response)
async def ping():
    """Server pinging"""
    return Response(result="pong")