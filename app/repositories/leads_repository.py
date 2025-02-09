from sqlalchemy.orm import Session
from app.models.leed_model import Lead
from app.schemas.lead_schema import LeadCreate


class LeadRepository:

    @staticmethod
    def get_all(db: Session):
        """Retrieve all leads from the database."""
        return db.query(Lead).all()

    @staticmethod
    def get_by_id(db: Session, lead_id: int):
        """Retrieve a lead by its ID."""
        return db.query(Lead).filter(Lead.id == lead_id).first()

    @staticmethod
    def create_leads(db: Session, leads_data: list):
        """Insert multiple leads into the database (used for initial data)."""
        for lead in leads_data:
            db.add(Lead(**lead))
        db.commit()

    @staticmethod
    def create(db: Session, lead_data: LeadCreate):
        """Create a new lead and return the created instance."""
        new_lead = Lead(**lead_data.dict())
        db.add(new_lead)
        db.commit()
        db.refresh(new_lead)  # Refresh to get the latest DB state
        return new_lead

    @staticmethod
    def update(db: Session, lead_id: int, lead_data: dict):
        """Update an existing lead if it exists."""
        lead = db.query(Lead).filter(Lead.id == lead_id).first()
        if not lead:
            return None
        for key, value in lead_data.items():
            setattr(lead, key, value)  # Update the attributes dynamically
        db.commit()
        db.refresh(lead)  # Refresh to reflect changes
        return lead

    @staticmethod
    def delete(db: Session, lead_id: int):
        """Delete a lead by its ID if it exists."""
        lead = db.query(Lead).filter(Lead.id == lead_id).first()
        if not lead:
            return None
        db.delete(lead)
        db.commit()
        return lead
