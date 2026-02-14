from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Shared base properties
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    

# Creating a Task (POST)
class TaskCreate(TaskBase):
    pass


# Updating a Task (PUT)
class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None


# Returning a Task (Response Model)
class TaskOut(TaskBase):
    id: int
    status: str
    created_at: datetime

    class Congif:
        orm_mode=True