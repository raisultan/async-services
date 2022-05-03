FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /service
COPY ./requirements.txt /service/requirements.txt

WORKDIR /service

RUN pip install -U pip && \
    pip install -r requirements.txt --src /usr/local/src 
