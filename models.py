from typing import Optional
from pydantic import BaseModel

class Posts(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None
    
class Person(BaseModel):
    fname: str
    name:str
    age:int
    occupationl:str


