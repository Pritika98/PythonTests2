FROM ubuntu:16.04

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
WORKDIR /app
COPY . /app

RUN python SampleTests.py
ENTRYPOINT ["python"]
