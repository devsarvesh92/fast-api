FROM python:3.10.4-alpine3.15

ENV PYTHONBUFFERED=1

WORKDIR /app
ADD requirements.txt requirements.txt

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY app /app

EXPOSE 8000

CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8000"]