FROM python:3.14.2-alpine

COPY requirements.txt /tmp

RUN pip install -r /tmp/requirements.txt

COPY ./src /app

WORKDIR /app

CMD ["python", "app.py"]