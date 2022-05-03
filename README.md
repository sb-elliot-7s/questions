1. docker-compose up -d --build
2. docker-compose run fastapi_app alembic revision --autogenerate -m "First migration"
3. docker-compose run fastapi_app alembic upgrade head
