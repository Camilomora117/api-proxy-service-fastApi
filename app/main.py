from fastapi import FastAPI

from app.config.config_postgres import Base, engine, Session
from app.controllers import users_controller, leads_controller
from app.middlewares.error_handler import ErrorHandler
from app.utils.load_database import init_leads

app = FastAPI()

## Add Table DB
Base.metadata.create_all(bind=engine)

## Add Leads Database Default
init_leads()

## Add middleware
app.add_middleware(ErrorHandler)

## Add Controllers
app.include_router(users_controller.user_controller)
app.include_router(leads_controller.leads_controller)

## Controller Test
@app.get("/")
def read_root():
    return {"message": "FastAPI is running!"}