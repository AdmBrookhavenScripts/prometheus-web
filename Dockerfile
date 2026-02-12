FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y \
    nodejs \
    npm \
    luajit \
    git \
    curl \
    && apt clean

WORKDIR /app

COPY . .

RUN npm install

RUN git clone https://github.com/prometheus-lua/Prometheus.git

EXPOSE 3000

CMD ["node", "server.js"]
