FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install -r /code/requirements.txt

COPY . .


#EXPOSE 8000
#
#CMD ["uvicorn", "main:app", "--reload", "--port", "8000"]
