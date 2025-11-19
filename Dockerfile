FROM python:3.11.5-alpine

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PATH="/PY/BIN:$PATH"

RUN pip install --upgrade pip

#COPY ./requirements.txt /app/requirements.txt
COPY . /app

RUN pip install -r requirements.txt
