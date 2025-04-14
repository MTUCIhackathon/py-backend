from fastapi import APIRouter, HTTPException
import logging
from model import GenerateModel
from schemas.ml import PersonalityTestInput, PersonalityTestResponse

router = APIRouter()
logger = logging.getLogger(__name__)

generator = GenerateModel()

@router.post("/", response_model=PersonalityTestResponse)
async def personality_test(test_input: PersonalityTestInput):
    try:
        result = generator.get_professions_personality_test(test_input.test_result)
        return PersonalityTestResponse(**result)
    except Exception as e:
        logger.error(f"Ошибка обработки теста MBTI: {e}")
        raise HTTPException(status_code=500, detail=str(e))
