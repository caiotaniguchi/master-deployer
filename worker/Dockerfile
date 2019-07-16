FROM python:3.7.4-stretch

COPY ./worker/ /app
COPY ./model/ /app/model
WORKDIR /app

RUN ["pip", "install", "-r", "/app/requirements.txt", "-r", "/app/model/requirements.txt"]

CMD ["python", "app.py"]
