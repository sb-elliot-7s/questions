from typing import Optional
from .repositories import QuestionRepositoryInterface
import aiohttp


class QuestionAPIService:
    def __init__(self, repository: QuestionRepositoryInterface):
        self._repository = repository
        self._url = 'https://jservice.io/api/random'

    async def _get_questions(self, question_nums: int) -> list[Optional[dict]]:
        async with aiohttp.ClientSession() as session:
            response = await session.get(url=self._url, params={'count': question_nums})
            if response.status == 200:
                return await response.json()

    async def save_questions(self, question_nums: int):
        raw_question_data = await self._get_questions(question_nums=question_nums)
        return await self._repository.save_question(questions_data=raw_question_data)
