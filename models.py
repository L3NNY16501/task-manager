from sqlalchemy import Column, Integer, String, Text, Enum, TIMESTAMP, func
from sqlalchemy.orm import declarative_base

# Define the declarative base
Base = declarative_base()

# Create models here for database tables
class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    status = Column(
        Enum("pending", "in_progress", "complete"),
        default="pending",
        nullable=False
    )
    created_at = Column(
        TIMESTAMP,
        server_default=func.now()
    )