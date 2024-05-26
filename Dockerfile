FROM python:3.12-alpine AS BASE

WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . /app

EXPOSE 9999

CMD ["python", "main.py"]
