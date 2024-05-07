# To-Do List Backend API Documentation

This document outlines the API endpoints and their functionalities for the To-Do List backend.

| Endpoint               | Method | Description                                  | Body Request           | Body Response         | Error Response                            |
|------------------------|--------|----------------------------------------------|------------------------|-----------------------|-------------------------------------------|
| `/createTask`          | POST   | Create a new task                           | Task object (JSON)     | Created task object   | `404 Not Found` if task not found         |
| `/getTaskID/{task_id}` | GET    | Get a task by its ID                        | -                      | Task object (JSON)    | `404 Not Found` if task not found         |
| `/getTaskTitle/{title}`| GET    | Get tasks by title                          | -                      | List of task objects  | `404 Not Found` if no tasks found         |
| `/deleteID/{task_id}`  | DELETE | Delete a task by its ID                     | -                      | Message (JSON)        | `404 Not Found` if task not found         |
| `/deleteTitle/{title}` | DELETE | Delete tasks by title                       | -                      | Message (JSON)        | `404 Not Found` if no tasks found         |
| `/deleteAll`           | DELETE | Delete all tasks                            | -                      | Message (JSON)        | -                                         |
| `/getAllTasks`         | GET    | Get all tasks                               | -                      | List of task objects  | -                                         |
| `/updateTask/{task_id}`| PUT    | Update a task by its ID                     | Task object (JSON)     | Message (JSON)        | `404 Not Found` if task not found         |