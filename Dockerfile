FROM python:3.9.1-slim
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get -y install cron
ADD crontab /etc/cron.d/crontab
RUN chmod 0644 /etc/cron.d/crontab

WORKDIR /code

COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /code/