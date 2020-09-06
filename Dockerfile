FROM python:3.8.2-alpine3.11 as base
FROM base as builder

WORKDIR /install

RUN apk update && apk add gcc postgresql-dev python3-dev musl-dev git zlib-dev build-base jpeg-dev  --no-cache

RUN /usr/local/bin/python -m pip install --upgrade pip

COPY requirements.txt /requirements.txt
RUN pip install --prefix=/install -r /requirements.txt

FROM base

RUN apk add libpq jpeg-dev --no-cache

COPY --from=builder /install /usr/local

WORKDIR /app

COPY aku_aku/ .

CMD python3 main.py

