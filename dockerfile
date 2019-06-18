FROM ubuntu:latest
MAINTAINER Mohit "mg909@snu.edu.in"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential libpq-dev postgresql-server-dev-all python-psycopg2
# RUN apt-get install telnet
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]