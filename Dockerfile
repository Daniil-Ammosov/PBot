FROM python:3.8-alpine3.13
LABEL maintainer=ammosov@tbdd.ru
USER root
WORKDIR /home/user/bot

# Copy project files to docker container
COPY . ./

# Prepare env
#RUN    apt update \
#       && DEBIAN_FRONTEND="noninteractive" apt install python3.8 python3-pip -y \

RUN    apk add build-base
RUN    python3.8 setup.py install

#RUN     /usr/local/bin/deploy_telegram_bot_db

ENTRYPOINT ["p_bot"]
