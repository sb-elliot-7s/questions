from abc import ABC, abstractmethod
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
            return True
        return False

    async def save_question(self, questions_data: list[dict]):
        if questions_data:
            _ = await self._session.execute(
                insert(Question).values([QuestionSchema(**question).dict() for question in questions_data]))
            await self._session.commit()
            return (await self._session.scalars(select(Question).where(Question.question_id == questions_data[-1].get('id')))).first()
        return {}
