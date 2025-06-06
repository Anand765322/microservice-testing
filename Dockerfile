FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install flask pytest pytest-cov requests jsonschema

EXPOSE 5000

CMD ["python", "app/app.py"]
