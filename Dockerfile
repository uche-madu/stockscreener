FROM python:3.10.10-slim as builder

RUN apt-get update && \
    apt-get install -y libpq-dev gcc
# set work directory
WORKDIR /app

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY requirements.txt .
RUN pip install -U pip
RUN pip install -r requirements.txt

# copy project
COPY . .

#FROM python:3.10.10-alpine3.17

#COPY --from=builder ./app ./
