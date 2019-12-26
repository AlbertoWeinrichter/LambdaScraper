FROM ubuntu:18.04
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get upgrade -y
RUN apt-get install build-essential cmake libgtk-3-dev libboost-all-dev python3-pip -y

RUN mkdir /backend
WORKDIR /backend
COPY requirements.txt /backend/
RUN pip3 install -r requirements.txt
ADD . /backend

RUN ls -all

EXPOSE 8000

# Wait for postgres
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.2.1/wait /wait
RUN chmod +x /wait
