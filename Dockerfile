# syntax=docker/dockerfile:1
FROM python:3.9 as requirements-stage

WORKDIR /tmp

RUN pip3 install poetry

COPY ./pyproject.toml ./poetry.lock* /tmp/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.9

WORKDIR /usr/src/core-services-api

RUN mkdir -p /root/.unlimiter

COPY /config/unlimiter.config.yaml /root/.unlimiter/config.yaml

COPY --from=requirements-stage /tmp/requirements.txt /usr/src/core-services-api/requirements.txt

RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

ARG GITHUB_TOKEN=""

RUN pip3 install  git+https://${GITHUB_TOKEN}@github.com/AbSciBio/unlimiter.git

COPY . /usr/src/core-services-api
