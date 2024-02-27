FROM ubuntu:latest
WORKDIR /app
COPY . /app
ENTRYPOINT ["python", "-m", "main"]