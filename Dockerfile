FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .

# Cria a pasta de entrada caso não exista
RUN mkdir -p /app/input

CMD ["python", "main.py"]