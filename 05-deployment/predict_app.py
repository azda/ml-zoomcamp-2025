import pickle
from fastapi import FastAPI
from pydantic import BaseModel

with open('pipeline_v1.bin', 'rb') as f_in:
    pipeline = pickle.load(f_in)

app = FastAPI(title="Lead Conversion Prediction API")

class Lead(BaseModel):
    lead_source: str
    number_of_courses_viewed: int
    annual_income: float

class PredictionResponse(BaseModel):
    conversion_probability: float
    will_convert: bool

@app.get("/")
def root():
    return {
        "message": "Lead Conversion Prediction API",
        "endpoints": {
            "predict": "/predict (POST)"
        }
    }


@app.post("/predict", response_model=PredictionResponse)
def predict(lead: Lead):
    lead_dict = lead.model_dump()
    probability = pipeline.predict_proba([lead_dict])[0, 1]
    
    return {
        "conversion_probability": probability,
        "will_convert": probability >= 0.5
    }
