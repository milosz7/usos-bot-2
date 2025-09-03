FROM python:3.13-slim

RUN pip install --no-cache-dir poetry
RUN apt-get update && apt-get install -y inotify-tools && apt-get clean

WORKDIR /src
COPY pyproject.toml poetry.lock* /src/

RUN poetry config virtualenvs.create false \
  && poetry lock && poetry install --no-root --no-interaction --no-ansi


COPY src/ /src
#CMD ["bash", "-c", "while true; do sleep 1 done"]
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
