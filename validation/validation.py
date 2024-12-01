from typing import List, Optional
from pydantic import BaseModel

class Coords(BaseModel):
    id: str
    timestamp: str
    label: str
    route: str
    value: int
    average_speed: float
    number_a: str
    latitude: float
    longitude: float
    do: int

class Person(BaseModel):
    id: int
    name: str
    date: str
    number_a: str
    rating: Optional[int] = None
    experience: Optional[int] = None
    count_tasks: Optional[int] = None
    
class Cargo(BaseModel):
    id: int
    name: str
    danger_lvl: int
    driver: int

class Werehouse(BaseModel):
    id: int
    address: str
    tags: List[str] = []
