%%writefile CRUD_API.py
from fastapi import FastAPI
from pydantic import BaseModel

# Initialize the FastAPI engine
app = FastAPI()

# Create a temporary database using a Python list
todo_list = []

class Task(BaseModel):
    id: int
    title: str
    is_done: bool = False

# Show all the saved tasks
@app.get("/tasks")
def get_all_tasks():
    return {"tasks": todo_list}

# Route path to create a new task
@app.post("/tasks")
def create_task(new_task: Task):
    todo_list.append(new_task)
    return {"message": "Task added successfully!"}

# Route path to update an existing task
@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task):
    for i in range(len(todo_list)):
        if todo_list[i].id == task_id:
            todo_list[i] = updated_task
            return {"message": "Task updated!"}
    return {"error": "Task not found"}

# Route Path to permanently delete a task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for i in range(len(todo_list)):
        if todo_list[i].id == task_id:
            del todo_list[i]
            return {"message": "Task deleted!"}
    return {"error": "Task not found"}
