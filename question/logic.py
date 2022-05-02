from .repositories import QuestionRepositoryInterface
import aiohttp
from fastapi import HTTPException, status


class QuestionAPIService:
    def __init__(self, repository: QuestionRepositoryInterface):
        self._repository = repository
        self._url = 'https://jservice.io/api/random'

    async def _get_questions(self, question_nums: int) -> list[dict]:
        async with aiohttp.ClientSession() as session:
            response = await session.get(url=self._url, params={'count': question_nums})
            if response.status == 200:
                return await response.json()
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='some error')

    async def check(self, question_nums: int):
        raw = await self._get_questions(question_nums=question_nums)
        if question_nums < 0:
            return []
        questions = []
        for index, question in enumerate(raw):
            result = await self._repository.get_question(question_id=question.get('id'))
            if result:
                print('duplicate')
                return await self.check(question_nums=question_nums - index)
            questions.append(question)
        return questions

    async def save_questions(self, question_nums: int):
        data = await self.check(question_nums=question_nums)
        return await self._repository.save_question(questions_data=data)
