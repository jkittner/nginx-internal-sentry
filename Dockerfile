FROM python:3.9-bullseye

WORKDIR /usr/src/app

COPY ./requirements.txt .

RUN python -m venv venv
RUN venv/bin/pip install --no-cache-dir -r requirements.txt

COPY app.py .
