FROM python:3.11-slim

WORKDIR /app

COPY requirememts.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "run.py"]