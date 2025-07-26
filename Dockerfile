FROM python:3.11-slim

WORKDIR /app

COPY requirememts.txt .
RUN pip install -r requirememts.txt

COPY . .

EXPOSE 8000

CMD ["python", "run.py"]