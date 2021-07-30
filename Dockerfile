FROM python:3.9.6-alpine3.11 as base
FROM base as builder

WORKDIR /install

RUN apk update && apk add gcc python3-dev musl-dev git zlib-dev build-base jpeg-dev  --no-cache

RUN /usr/local/bin/python -m pip install --upgrade pip

COPY requirements.txt /requirements.txt
RUN pip install --prefix=/install -r /requirements.txt

FROM base

RUN apk add jpeg-dev --no-cache

COPY --from=builder /install /usr/local

WORKDIR /app

COPY . .

RUN pip3 install .

CMD python3 merlin

#todo uvicorn?
