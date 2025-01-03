from typing import Optional
from pydantic import BaseModel
class Blog_Pyd(BaseModel):
    id : int
    name : str
    price : float
    author : Optional[str] = None

    class Config:
        orm_mode = True

class Blog_up(BaseModel):
    id : int
    name : Optional[str]
    price : Optional[float] = None
    author : Optional[str]