from typing import List

from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import JSONResponse
from app.config.config_postgres import Session
from app.schemas.lead_schema import LeadResponse, LeadCreate
from app.services.leads_service import LeadService
from app.utils.logger import get_logger
from app.utils.session_db import get_db

leads_controller = APIRouter()
logger = get_logger("LeadController")


@leads_controller.get(
    path="/leads",
    summary="Get All Leeds",
    tags=["User"],
    response_model=List[LeadResponse])
def get_all_leads(db: Session = Depends(get_db)):
    """Get All Lead"""
    try:
        logger.info("Init get lead controller")
        service = LeadService(db)
        leads = service.get_all_leads()
        leads_json = [LeadResponse.model_validate(lead).model_dump() for lead in leads]
        return JSONResponse(content={"leads": leads_json}, status_code=status.HTTP_200_OK)
    except Exception as err:
        logger.exception(f"Error Get Leads: {err}")
        raise HTTPException(status_code=500, detail=str(err))


@leads_controller.post(
    path="/leads",
    summary="Create a new lead",
    tags=["Leads"])
def create_lead(lead_data: LeadCreate, db: Session = Depends(get_db)):
    """Create a new lead and store it in the database."""
    try:
        logger.info("Init create lead controller")
        service = LeadService(db)
        service.create_lead(lead_data)
        return JSONResponse(
            content={"message": "Lead created successfully"},
            status_code=201
        )
    except Exception as err:
        logger.exception(f"Error Create Lead: {err}")
        raise HTTPException(status_code=500, detail=str(err))