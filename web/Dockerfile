
FROM python:3.6.8-alpine

LABEL get web service up and running

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

WORKDIR /app

CMD python /src/main.py