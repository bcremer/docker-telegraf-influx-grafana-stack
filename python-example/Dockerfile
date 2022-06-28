FROM python:3.9.10

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY ["./app",  "."]

RUN pip3 install -r requirements.txt


CMD ["uvicorn", "app:app", "--reload", "--host=0.0.0.0", "--port=8000"]