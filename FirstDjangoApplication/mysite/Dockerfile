FROM python:3.7-alpine

WORKDIR /app
COPY . /app
ENV PYTHON_ENV docker

RUN apk update && \
apk add postgresql-dev gcc python3-dev musl-dev && \
apk add git && \
pip install -r requirements.txt
RUN apk add --no-cache --upgrade bash
EXPOSE 5432  22 443 9418 6379
