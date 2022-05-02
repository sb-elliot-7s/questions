from abc import ABC, abstractmethod
from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert, select
from .models import Question
from .schemas import QuestionSchema


class QuestionRepositoryInterface(ABC):

    @abstractmethod
    async def get_question(self, question_id: int): pass

    @abstractmethod
    async def save_question(self, questions_data: list[dict]): pass


class QuestionRepository(QuestionRepositoryInterface):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_question(self, question_id: int):
        result = await self._session.execute(select(Question).where(Question.question_id == question_id))
        if _ := result.scalars().first():
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Question is exists')
        return False

    async def save_question(self, questions_data: list[dict]):
        result = None
        if questions_data:
            for question in questions_data:
                await self.get_question(question_id=question.get('id'))
                result = await self._session.execute(insert(Question).values(**QuestionSchema(**question).dict()).returning(Question))
            await self._session.commit()
        return result.first() if result else {}
