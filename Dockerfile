FROM python:3.8

RUN mkdir /app
WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt
ENV DJANGO_SETTINGS_MODULE=project.settings
RUN python manage.py collectstatic --noinput
RUN python manage.py migrate

RUN python manage.py create_superuser
EXPOSE 80

CMD gunicorn --bind=0.0.0.0:80 --forwarded-allow-ips="*" project.wsgi