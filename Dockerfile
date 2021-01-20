FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
COPY requirements.django.txt /code/

# RUN pip install -r requirements.txt
RUN pip install -r requirements.django.txt
RUN pip install psycopg2-binary
COPY timesheet /code/