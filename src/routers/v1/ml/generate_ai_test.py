from fastapi import APIRouter, HTTPException
import logging
from model import GenerateModel
from schemas.ml import GenerateAITestInput, GenerateAITestResponce, ResultAITestInput, ResultAITestResponce

router = APIRouter()
logger = logging.getLogger(__name__)

generator = GenerateModel()

@router.post("/generate_AI_test", response_model=GenerateAITestResponce)
async def generate_AI_test(test_input: GenerateAITestInput):
    try:
        result = generator.generate_ai_test(answers_history=test_input.questions)
        return GenerateAITestResponce(**result)
    except Exception as e:
        logger.error(f"Ошибка генерации теста: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/summarize_AI_test", response_model=ResultAITestResponce)
async def summarize_AI_test(test_input: ResultAITestInput):
    try:
        result = generator.get_professions_ai_test(answers_history=test_input.user_answers)
        return ResultAITestResponce(**result)
    except Exception as e:
        logger.error(f"Ошибка получения результатов сгенерированного теста: {e}")
        raise HTTPException(status_code=500, detail=str(e))