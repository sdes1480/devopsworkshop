From ubuntu:latest
RUN apt-get update && apt-get install -y python3-pip
RUN apt-get install -y git
RUN pip3 install folium && pip3 install get
RUN mkdir /code && cd /code

