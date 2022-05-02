from datetime import datetime

from pydantic import BaseModel, Field, validator


class QuestionNums(BaseModel):
    questions_num: int = 1


class QuestionSchema(BaseModel):
    question_id: int = Field(alias='id')
    question: str
    answer: str
    created_at: datetime
    category_id: int

    @validator('created_at', pre=True)
    def datetime_validate(cls, value):
        return datetime.fromisoformat(value.replace('Z', '')).replace(microsecond=0)

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
