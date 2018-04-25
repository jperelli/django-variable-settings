FROM python:2.7

ENV PYTHONUNBUFFERED 1

RUN pip install "Django>=1.11.0,<1.12.0".

ADD ./example_project /app
ADD ./variable_settings /packages/variable_settings
ADD ./variable_settings /app/variable_settings

ENV PYTHONPATH /packages/
WORKDIR /app

ENTRYPOINT ./docker-entrypoint.sh
