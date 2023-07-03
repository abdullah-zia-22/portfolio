FROM python:3.10

ENV FLASK_APP=wsgi.py
ENV FLASK_ENV=development

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .

CMD [ "waitress-serve", "wsgi:app" ]