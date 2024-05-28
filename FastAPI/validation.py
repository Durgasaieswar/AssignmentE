from pydantic import BaseModel

class ValidatePayload(BaseModel):

    long: float
    lat: float

