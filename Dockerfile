FROM python:3.10

RUN apt-get update && apt-get install -y lua5.1 git

WORKDIR /app

COPY . .

RUN git clone https://github.com/prometheus-lua/Prometheus.git

RUN pip install flask

EXPOSE 5000

CMD ["python", "app.py"]
