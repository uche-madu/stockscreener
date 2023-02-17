FROM python:3.10.10-slim as builder

# set work directory
WORKDIR /app

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install -U pip
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . /app/

