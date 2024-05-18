from pydantic import BaseModel


class Car(BaseModel):
    Year: int
    Kilometer: int
    Fuel: int
    Transmission: int
    Owner: int
    Mileage: int
    Engine: int
    Seats: int
    Price: int