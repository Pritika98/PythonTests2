FROM python:3
WORKDIR /app
COPY . /app

RUN python SampleTests.py 

CMD ["python"]
