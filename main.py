from fastapi import FastAPI,Depends
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def index():
    return {"result":"hello"}


#  path parameters

@app.get('/about/{id}')
def about(id: int):
    return {"id":id}

@app.get('/about/profile')
def about(id):
    return {"id":id}
# here this wont work as we have defined a same url with int type above : to make it work we need to move above to that


# query parameters

@app.get('/index')
def get_blogs(limit:int,offset:int = 10, sort:Optional[bool] = None):
    return {limit:offset+limit}

# always default args should follow last 

#  we can also import optional from typing , and we can use conditions like bool and write the condition based code


# @app.get('/index')
# def get_blogs(limit:str,offset:int = 10):
#     return {limit:offset+limit}

# this will give internal server error


# pydantic schema  -- request body

# fast api has a built in support for data validation for request body 

# it uses pydantic base model to  define request body schema 

# we can also use Dict and Any to avoid predefined schema

class Blog_Pyd(BaseModel):
    id : int
    name : str
    price : float
    author : Optional[str] = None

    class Config:
        orm_mode = True



    