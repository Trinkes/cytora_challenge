FROM python:3.12.1-slim
WORKDIR /app
COPY . /app
ENTRYPOINT ["python", "-m", "src.main"]