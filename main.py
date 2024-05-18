from fastapi import FastAPI
from ML_model.suggest_generator import create_sugestion
from ML_model.dto import Car
import pandas as pd
import json

cars_data = pd.read_csv("ML_model/Data_agrupada.csv")

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/predict/")
async def predict(car: Car):
    suggestion = create_sugestion(car.Year,car.Kilometer,car.Fuel,car.Transmission,car.Owner,car.Mileage,car.Engine,car.Seats,car.Price)
    mask = cars_data['Group'].isin([suggestion[0]])
    recomendation = {
        "Name": str(cars_data[mask]['Name'].iloc[0]),
        "Year": str(cars_data[mask]['Year'].iloc[0]),
        "Kilometers_Driven": str(cars_data[mask]['Kilometers_Driven'].iloc[0]),
        "Fuel_Type": str(cars_data[mask]['Fuel_Type'].iloc[0]),
        "Transmission": str(cars_data[mask]['Transmission'].iloc[0]),
        "Owner_Type": str(cars_data[mask]['Owner_Type'].iloc[0]),
        "Mileage": str(cars_data[mask]['Mileage'].iloc[0]),
        "Engine": str(cars_data[mask]['Engine'].iloc[0]),
        "Seats": str(cars_data[mask]['Seats'].iloc[0]),
        "Price": str(cars_data[mask]['Price'].iloc[0])
    }
    return {json.dumps(recomendation)}