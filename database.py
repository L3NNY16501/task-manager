from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
import os
from dotenv import load_dotenv

# Load Environment Variables
load_dotenv()

# Build Database URL
DB_URL = (
    f"mysql+pymysql://"
    f"{os.getenv('DB_USER')}:"
    f"{os.getenv('DB_PASS')}@"
    f"{os.getenv('DB_HOST')}/"
    f"{os.getenv('DB_NAME')}"
)

# Create SQLAlchemy Engine
engine = create_engine(DB_URL, echo=True)

# Create Session Factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Dependency for FastAPI
# Creates a database session per request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()