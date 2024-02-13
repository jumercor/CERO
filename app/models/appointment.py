from pydantic import BaseModel

class Appointment(BaseModel):
    id: int
    date: str
    time: str
    client_name: str
    status: str