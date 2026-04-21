from fastapi import FastAPI, Query
from pydantic import BaseModel


class Item(BaseModel):
    id: int
    title: str
    description: str

app = FastAPI()

# How can we know the the body parameter

# if u define a parameter in your path it's means it is path parameter 
# if it has singular type as we provide to {data}👇 so it's means it is query parameter!
# if u use pydantic and define custom type so it's means it is body parameter!

         
@app.get("/student/{id}/assignments/{assignment_id}")
def StudentData(id:int, assignment_id:int, data:int, item:Item):
    return item


@app.get("/validation")
# we can use this to validate user input in query parameter and body parameter as well

# and this regex pattern means that the name should only contain letters and should be between 5 and 10 letters!

def Validation(name: str = Query (max_length=10, min_length=5, regex="^[a-zA-Z]+$")):
    return {"name": name}