from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, List

app = FastAPI()

# Allowing CORS (Cross-Origin Resource Sharing) for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Model for Task
class Task(BaseModel):
    id: int
    title: str
    completed: bool = False

# In-memory database for tasks
task_id_count = 0
tasks: Dict[int, Task] = {}

# Create a task
@app.post("/createTask")
def create_task(task: Task):
    global task_id_count
    task_id = task_id_count
    task.id = task_id
    tasks[task_id] = task
    task_id_count += 1
    return task

# Get task by ID
@app.get("/getTaskID/{task_id}")
def get_task_by_id(task_id: int):
    task = tasks.get(task_id)
    if task:
        return task
    else:
        raise HTTPException(status_code=404, detail="Task not found")

# Get task by title
@app.get("/getTaskTitle/{title}")
def get_task_by_title(title: str):
    filtered_tasks = [task for task in tasks.values() if task.title == title]
    if filtered_tasks:
        return filtered_tasks
    else:
        raise HTTPException(status_code=404, detail=f"No tasks found with title '{title}'")

# Delete task by ID
@app.delete("/deleteID/{task_id}")
def delete_task_by_id(task_id: int):
    if task_id in tasks:
        del tasks[task_id]
        return {"message": "Task deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Task not found")

# Delete task by title
@app.delete("/deleteTitle/{title}")
def delete_task_by_title(title: str):
    tasks_to_delete = [task_id for task_id, task in tasks.items() if task.title == title]
    if tasks_to_delete:
        for task_id in tasks_to_delete:
            del tasks[task_id]
        return {"message": f"All tasks with title '{title}' deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail=f"No tasks found with title '{title}'")

# Delete all tasks
@app.delete("/deleteAll")
def delete_all_tasks():
    tasks.clear()
    return {"message": "All tasks deleted successfully"}

# Get all tasks
@app.get("/getAllTasks", response_model=List[Task])
def get_all_tasks():
    return list(tasks.values())

# Update task by ID
@app.put("/updateTask/{task_id}")
def update_task(task_id: int, updated_task: Task):
    if task_id in tasks:
        tasks[task_id] = updated_task
        return {"message": "Task updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="Task not found")
