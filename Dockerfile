FROM python:3.13-slim

RUN pip install --no-cache-dir poetry

WORKDIR /src
COPY pyproject.toml poetry.lock* /src/

RUN poetry config virtualenvs.create false \
  && poetry lock && poetry install --no-root --no-interaction --no-ansi


COPY src/ /src

CMD ["python", "main.py"]
