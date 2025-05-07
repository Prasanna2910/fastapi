from fastapi import FastAPI

api = FastAPI()

allTodos = [
    {"todo_id":1,"todo_name":"Sports","description":"Gym"},
    {"todo_id":2,"todo_name":"Read","description":"10 pages"},
    {"todo_id":3,"todo_name":"Shop","description":"buy cloths"},
    {"todo_id":4,"todo_name":"Study","description":"exam"},
    {"todo_id":5,"todo_name":"Meditate","description":"2 mins"},
]

@api.get("/")
def index():
    return {"message" : "Hello world"}

@api.get("/todos/{todo_id}")
def get_todo(todo_id:int):
    for todo in allTodos:
        if todo["todo_id"] == todo_id:
            return {"result":todo}
        
        

@api.get("/todos")
def get_todo(first_n:int = None):
    if first_n:
        return allTodos[:first_n]
    else:
        return allTodos

@api.post("/todos")
def create_todo(todo:dict):
    new_todo_id = max(todo["todo_id"] for todo in allTodos) +1

    new_todo = {
        "todo_id" :new_todo_id,
        "todo_name": todo["todo_name"],
        "todo_description" : todo['todo_description']
    }

    allTodos.append(new_todo)

    return new_todo

@api.put("/todos/{todo_id}")
def update_todo(todo_id : int,updated_todo:dict):
    for todo in allTodos:
        if todo["todo_id"] == todo_id:
            todo["todo_name"] = update_todo["todo_name"]
            todo["todo_description"] = update_todo["todo_description"]
            return todo
    return "Not found"

@api.delete("/todod/{todo_id}")
def delte_todo(todo_id : int):
    for index,todo in enumerate(allTodos):
        if todo["todo_id"] == todo_id:
            deleted_todo = allTodos.pop(index)
            return deleted_todo
    return "Error" 