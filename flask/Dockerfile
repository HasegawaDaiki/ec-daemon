FROM debian:latest

RUN mkdir /app

WORKDIR /app

COPY . /app

RUN cat ./debian-sources-add.txt >> /etc/apt/sources.list.d/debian.sources

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    net-tools \
    nano \
    procps \
    ufw \
    git \
    python3 \
    python3-flask \
    python3-werkzeug \
    python3-mysql.connector \
    mosquitto \
    mosquitto-clients \
    gunicorn

RUN git config --global user.name "HasegawaDaiki"

RUN git config --global user.email "schroeder.118@gmail.com"

RUN chown -R mosquitto:mosquitto /var/log/mosquitto

RUN chown -R mosquitto:mosquitto /var/lib/mosquitto

RUN chown -R mosquitto:mosquitto /etc/mosquitto

RUN mosquitto -p 1884 -d

RUN chown -R gunicorn:gunicorn /var/log/gunicorn

CMD ["gunicorn", "--config", "gunicorn/settings.py", "app:app"]