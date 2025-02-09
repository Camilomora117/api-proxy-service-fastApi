from pydantic import BaseModel
from typing import Optional

class Address(BaseModel):
    street: str
    suite: str
    city: str
    zipcode: str

class User(BaseModel):
    id: int
    name: str
    username: str
    email: str
    address: Optional[Address]

class UserFilter(BaseModel):
    filter_key: str
    filter_value: str