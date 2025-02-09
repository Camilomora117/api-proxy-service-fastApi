from pydantic import BaseModel

class LeadResponse(BaseModel):
    id: int
    name: str
    location: str
    budget: int

    class Config:
        from_attributes = True

class LeadCreate(BaseModel):
    name: str
    location: str
    budget: int