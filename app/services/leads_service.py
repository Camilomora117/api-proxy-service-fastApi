from sqlalchemy.orm import Session
from app.repositories.leads_repository import LeadRepository
from app.schemas.lead_schema import LeadCreate


class LeadService:

    def __init__(self, db: Session):
        self.db = db

    def get_all_leads(self):
        """Get All lead"""
        return LeadRepository.get_all(self.db)

    def create_lead(self, lead_data: LeadCreate):
        """Create New lead"""
        return LeadRepository.create(self.db, lead_data)

    def filter_leads(self, location: str = None, min_budget: float = None, max_budget: float = None):
        """Filter leads by location and/or budget range."""
        leads = self.get_all_leads()

        if location:
            leads = [lead for lead in leads if lead.location.lower() == location.lower()]

        if min_budget is not None:
            leads = [lead for lead in leads if lead.budget >= min_budget]

        if max_budget is not None:
            leads = [lead for lead in leads if lead.budget <= max_budget]

        return leads

    def calculate_total_budget(self, leads):
        """Calculate the total budget of the filtered leads."""
        return sum(lead.budget for lead in leads)

    def sort_leads_by_budget(self, leads, descending=True):
        """Sort leads by budget in descending (default) or ascending order."""
        return sorted(leads, key=lambda lead: lead.budget, reverse=descending)

    def present_results(self, location: str = None, min_budget: float = None, max_budget: float = None):
        """Filter, sort, and calculate total budget, then return results."""
        filtered_leads = self.filter_leads(location, min_budget, max_budget)
        sorted_leads = self.sort_leads_by_budget(filtered_leads)
        total_budget = self.calculate_total_budget(filtered_leads)

        return {
            "filtered_leads": sorted_leads,
            "total_budget": total_budget
        }