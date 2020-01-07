FROM python:3.9.0a2-alpine3.10
ENV PYTHONUNBUFFERED 1
RUN mkdir /wapp
WORKDIR /wapp
COPY requirements.txt /wapp/
COPY . /wapp/
RUN pip install -r requirements.txt
COPY . .

