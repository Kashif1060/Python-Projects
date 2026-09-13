%%writefile capstone_project.py
from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker

# 1. Create the FastAPI app
app = FastAPI()

# 2. Database location
DATABASE_URL = "sqlite:///./todo.db"

# 3. Connect to the database 
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# 4. Base = blueprint for models; Session = helps modify the data
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 5. Define the table (ORM model)
class TaskDB(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    is_done = Column(Boolean, default=False)

# 6. Create the table in SQLite
Base.metadata.create_all(bind=engine)

# 7. Pydantic model to validate incoming data
class Task(BaseModel):
    id: int
    title: str
    is_done: bool = False

# 8. CREATE — add a new task
@app.post("/tasks")
def create_task(task: Task):
    db = SessionLocal()
    new_task = TaskDB(id=task.id, title=task.title, is_done=task.is_done)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    db.close()
    return new_task

# 9. READ — get all tasks
@app.get("/tasks")
def get_tasks():
    db = SessionLocal()
    tasks = db.query(TaskDB).all()
    db.close()
    return tasks
  
# 10. UPDATE — change an existing task's info
@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task):
    db = SessionLocal()
    task = db.query(TaskDB).filter(TaskDB.id == task_id).first()
    if task is None:
        db.close()
        return {"error": f"No task found with id {task_id}"}

    task.title = updated_task.title
    task.is_done = updated_task.is_done
    db.commit()
    db.refresh(task)
    db.close()

    return task


# 11. DELETE — remove a task completely
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    db = SessionLocal()
    task = db.query(TaskDB).filter(TaskDB.id == task_id).first()
    if task is None:
        db.close()
        return {"error": f"No task found with id {task_id}"}

    db.delete(task)
    db.commit()
    db.close()

    return {"message": f"Task {task_id} was deleted"}
