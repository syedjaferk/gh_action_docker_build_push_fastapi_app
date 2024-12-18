FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./random_id_generator ./random_id_generator
COPY app.py app.py

EXPOSE 8080

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]