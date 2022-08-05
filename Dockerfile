# pull official base image
FROM python:3.7.9-buster

# set work directory
WORKDIR /code

# install psycopg2 dependencies
RUN apt-get update && apt-get install -y gcc 

# build-essential python3-dev python3-pip python3-setuptools python3-wheel python3-cffi libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . /code/

# set environment variables
ENV PYTHONUNBUFFERED 1