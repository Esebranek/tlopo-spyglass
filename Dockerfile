FROM python:3.8-alpine

RUN mkdir -p app

COPY requirements.txt .

RUN pip install -r requirements.txt

WORKDIR /app

COPY ./spyglass ./spyglass

CMD gunicorn --chdir spyglass -w 2 app:application -b 0.0.0.0:8000
