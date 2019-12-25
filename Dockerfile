FROM python:3.9.0a2-alpine3.10
ENV PYTHONUNBUFFERED 1
RUN mkdir /wapp
WORKDIR /wapp
COPY requirements.txt /wapp/
COPY . /wapp/
RUN \
 apk add --no-cache python3 postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc python3-dev musl-dev postgresql-dev && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps

COPY . .

