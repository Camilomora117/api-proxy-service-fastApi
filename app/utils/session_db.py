from app.config.config_postgres import Session

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()