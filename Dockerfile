FROM python:3.10-bookworm

USER root

RUN apt-get update -y &&\
    apt-get install -y sudo &&\
    useradd -ms /bin/bash python &&\
    usermod -aG sudo python

WORKDIR /home/python

COPY ./src ./src

RUN pip install -r src/requirements.txt
