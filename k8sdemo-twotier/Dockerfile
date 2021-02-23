#set base image
FROM alpine:latest

#Install the required pakages
RUN apk add --no-cache python3
RUN apk add --no-cache py3-pip

#set the working directory in the container
WORKDIR /web

#copy the dependencies file to the working directory
COPY requirements.txt .

#install dependencies
RUN pip3 install -r requirements.txt

#copy the src code to the working directory
COPY web/ .
