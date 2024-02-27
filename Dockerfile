FROM python:3.12.1-slim as base

WORKDIR /app
COPY . /app

FROM base as tests
RUN pip install pytest
RUN ls -la
ENTRYPOINT ["pytest", "tests"]


FROM base as deps
ENTRYPOINT ["python", "-m", "src.main"]