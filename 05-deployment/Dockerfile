FROM agrigorev/zoomcamp-model:2025

WORKDIR /app

COPY pyproject.toml .
COPY 05-deployment/predict_app.py .
COPY 05-deployment/pipeline_v1.bin .

RUN pip install -e .

EXPOSE 8000

CMD ["uvicorn", "predict_app:app", "--host", "0.0.0.0", "--port", "8000"]
