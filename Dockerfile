FROM python:3.8

RUN mkdir /app
WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt
RUN python manage.py collectstatic --noinput

EXPOSE 80

CMD gunicorn --bind=0.0.0.0:80 --forwarded-allow-ips="*" project.wsgi