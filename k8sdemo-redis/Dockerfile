#set base image
FROM alpine:latest

#Install the required pakages
RUN apk add --no-cache python3 py3-pip redis supervisor

#set the working directory in the container
WORKDIR /web

#copy the dependencies file to the working directory
COPY requirements.txt .
COPY service_script.conf .

#install dependencies
RUN pip3 install -r requirements.txt

#copy the src code to the working directory
COPY web/ .

# Initializing Redis server and Gunicorn server from supervisord
CMD ["supervisord","-c","service_script.conf"]
