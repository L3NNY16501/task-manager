from fastapi import FastAPI
from database import engine
import tables
from routers import tasks
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Task Manager API")


# Create tables in Database
tables.Base.metadata.create_all(bind=engine)


# Add CORS Middleware (for frontend interaction)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# Include Task Routers
app.include_router(tasks.router)