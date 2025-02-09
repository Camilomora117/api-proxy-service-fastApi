from sqlalchemy import Column, Integer, String
from app.config.config_postgres import Base

class Lead(Base):
    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    budget = Column(Integer, nullable=False)
