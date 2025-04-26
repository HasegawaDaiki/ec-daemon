FROM nginx:latest

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    openssl 

COPY ./mqtt.conf /

RUN cat ./mqtt.conf >> /etc/nginx/nginx.conf

RUN chown nginx:nginx /etc/nginx

RUN chown nginx:nginx /var/log/nginx

RUN mkdir /etc/nginx/ssl

RUN openssl genrsa -out /etc/nginx/ssl/server.key 2048

RUN openssl req -new -key /etc/nginx/ssl/server.key -subj "/C=JP/ST=Tottori/L=Hokuei/O=Person/OU=Person/CN=kiri/E=schroeder.118@gmail.com/" -out etc/nginx/ssl/server.csr

RUN openssl x509 -days 3650 -req -signkey /etc/nginx/ssl/server.key -in /etc/nginx/ssl/server.csr -out /etc/nginx/ssl/server.crt

RUN service nginx start