FROM python:3.10-slim

WORKDIR /home/app

COPY . .

RUN pip install -r requirements.txt

VOLUME /home/app/data

CMD python main.py