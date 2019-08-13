FROM python:3.7.4-stretch

COPY ./api/ /app

COPY ./model/ /app/model

WORKDIR /app

RUN ["pip", "install", "-r", "/app/requirements.txt", "-r", "/app/model/requirements.txt"]

CMD ["gunicorn", "--reload", "-b", "0.0.0.0:8080", "app"]
