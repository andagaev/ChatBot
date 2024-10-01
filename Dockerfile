FROM python:3.11

WORKDIR /code

ARG TG_TOKEN
ARG DISCORD_TOKEN
ARG DATABASE_URL
ARG FILE_PATH

ENV PYTHONPATH=/code:/code/src
ENV TG_TOKEN=${TG_TOKEN}
ENV DISCORD_TOKEN=${DISCORD_TOKEN}
ENV DATABASE_URL=${DATABASE_URL}
ENV FILE_PATH=${FILE_PATH}

COPY poetry.lock pyproject.toml /code/
RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

COPY . /code/

CMD ["python", "src/main.py"]