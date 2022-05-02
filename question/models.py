from database import Base
import sqlalchemy as sa


class Question(Base):
    __tablename__ = 'questions'

    # id = sa.Column(sa.Integer, primary_key=True, index=True)
    question_id = sa.Column(sa.Integer, primary_key=True, index=True)
    question = sa.Column(sa.String)
    answer = sa.Column(sa.String)
    created_at = sa.Column(sa.DateTime)
    category_id = sa.Column(sa.Integer)

    def __repr__(self) -> str:
        return f'Question: {self.question_id} {self.question} - answer {self.answer}'
