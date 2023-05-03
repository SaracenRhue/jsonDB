FROM python:3.10-slim

WORKDIR /home/app

COPY . .

RUN pip install -r requirements.txt

ENV PORT=3000
EXPOSE 3000

VOLUME /home/app/data

CMD python main.py