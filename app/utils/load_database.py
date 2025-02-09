from app.config.config_postgres import Session
from app.models.leed_model import Lead
from app.utils.logger import get_logger

logger = get_logger("LoadDatabase")

leads_data = [
    {"id": 1, "name": "Ana Salcedo", "location": "Medellín", "budget": 200000000},
    {"id": 2, "name": "Santiago Gallo", "location": "Medellín", "budget": 500000000},
    {"id": 3, "name": "Carlota Habib", "location": "Medellín", "budget": 650000000},
    {"id": 4, "name": "Pablo Sánchez", "location": "Bogotá", "budget": 350000000},
    {"id": 5, "name": "Andrés Arias", "location": "Bogotá", "budget": 150000000},
    {"id": 6, "name": "Andrés Limas", "location": "Bogotá", "budget": 450000000},
]

def init_leads():
    """ Insert default leads if they do not exist """
    db = Session()
    if not db.query(Lead).first():
        lead_objects = [Lead(**lead) for lead in leads_data]
        db.add_all(lead_objects)
        db.commit()
    db.close()