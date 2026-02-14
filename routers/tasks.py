from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, schemas
from database import get_db

router = APIRouter(prefix="/tasks", tags=["tasks"])


#---- GET /tasks ----
@router.get("/", response_model=list[schemas.TaskOut])
def read_tasks(db: Session = Depends(get_db)):
    return crud.get_tasks(db)


#---- GET /tasks/{task_id} ----
@router.get("/{task_id}", response_model=schemas.TaskOut)
def read_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found.")
    return task

 
#---- Post /tasks ----
@router.post("/", response_model=schemas.TaskOut)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_new_task(db, task)


#---- PUT /tasks/{task_id} ----
@router.put("/{task_id}", response_model=schemas.TaskOut)
def update_task(task_id: int, task: schemas.TaskUpdate, db: Session = Depends(get_db)):
    updated_task = crud.update_task(db, task_id, task)
    if not updated_task:
        raise HTTPException(status_code=404, detail="Task not found.")
    return updated_task


#---- DELETE /tasks/{task_id} ----
@router.delete("/{task_id}", response_model=schemas.TaskOut)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    deleted_task = crud.delete_task(db, task_id)
    if not deleted_task:
        raise HTTPException(status_code=404, detail="Task not found.")
    return deleted_task