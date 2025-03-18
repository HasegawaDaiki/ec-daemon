FROM debian:latest

RUN mkdir /app

WORKDIR /app

COPY . /app

RUN cat debian-sources-add.txt >> /etc/apt/sources.list.d/debian.sources

RUN apt-get update

RUN apt-get install -y git

RUN git config --global user.name "kiri"
RUN git config --global user.email "schroeder.118@gmail.com"

RUN apt-get install -y python3

RUN apt-get install -y python3-flask

RUN apt-get install -y python3-werkzeug

RUN apt-get install -y python3-mysql.connector