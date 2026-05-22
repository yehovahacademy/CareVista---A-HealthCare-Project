from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from auth import router as auth_router



app = FastAPI()
app.include_router(auth_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class bmi(BaseModel):
  height: float
  weight: float
  status: str

class hydration(BaseModel):  
  water: float
  goal: float
  result: str
  


@app.get('/')
def greet():
  return {"Message: Your backend is running"}


@app.get('/bmi')
def calculate_bmi(weight: float, height: float):

    bmi = weight / (height * height)

    if bmi < 18.5:
        status = "Underweight"

    elif bmi < 25:
        status = "Healthy"

    elif bmi < 30:
        status = "Overweight"

    else:
        status = "Obese"

    return {
        "bmi": round(bmi, 2),
        "status": status
    }

@app.get('/hydration')
def calculate_hydration(water: float, goal: float):
    ratio = water / goal

    if ratio < 0.65:
        result = "Please drink some water"
    elif ratio >= 0.65:
        result = "Well done, you are hydrated enough!"

    return {
        'water': water,
        'goal': goal,
        'ratio': round(ratio, 2),
        'status': result
    }


#For user registration










     