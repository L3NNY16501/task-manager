from sqlalchemy.orm import Session
from models import Task
from schemas import TaskCreate, TaskUpdate


# ---- READ: GET TASKS ----
def get_tasks(db: Session):
    return db.query(Task).all()


# ---- READ: GET TASK BY ID ----
def get_task(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()

    
# ---- CREATE: ADD NEW TASK ----
def create_new_task(db: Session, task: TaskCreate):
    db_task = Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


# ---- UPDATE: MODIFY EXISTING TASK ----
def update_task(db: Session, task_id: int, task: TaskUpdate):
    """Searches for task by ID and then updates"""
    db_task = get_task(db, task_id)
    if not db_task:
        return None
    
    for key, value in task.dict(exclude_unset=True).items():
        setattr(db_task, key, value)
        
    db.commit()
    db.refresh(db_task)
    return db_task


# ---- DELETE: REMOVE TASK ----
def delete_task(db: Session, task_id: int):
    db_task = get_task(db, task_id)
    if not db_task:
        return None
    
    db.delete(db_task)
    db.commit()
    return db_task