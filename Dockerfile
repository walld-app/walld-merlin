FROM python:3.8.2-alpine3.11
RUN apk update && apk add gcc postgresql-dev python3-dev musl-dev git zlib-dev build-base jpeg-dev --no-cache
RUN /usr/local/bin/python -m pip install --upgrade pip
# ADD BUILDER AND WORKER
WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY aku_aku .

CMD python3 main.py

