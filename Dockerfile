FROM python:3.11
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

EXPOSE 6027

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "6027"]
