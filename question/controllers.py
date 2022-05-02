from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_session
from .logic import QuestionAPIService
from .repositories import QuestionRepository
from .schemas import QuestionNums

question_router = APIRouter(prefix='/question', tags=['question'])


@question_router.post('/', status_code=status.HTTP_201_CREATED)
async def some(question_nums: QuestionNums, session: AsyncSession = Depends(get_session)):
    return await QuestionAPIService(repository=QuestionRepository(session=session)).save_questions(question_nums=question_nums.questions_num)
