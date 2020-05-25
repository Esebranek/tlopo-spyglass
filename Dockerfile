FROM python:3.8-alpine

RUN echo "Etc/UTC" >  /etc/timezone

RUN apk add --no-cache -q build-base libffi-dev

RUN mkdir -p app

COPY requirements.txt .

RUN pip install -r requirements.txt

WORKDIR /app

COPY ./spyglass ./spyglass

EXPOSE 8000

CMD gunicorn --chdir spyglass -k geventwebsocket.gunicorn.workers.GeventWebSocketWorker -w 1 app:application -b 0.0.0.0:8000
