from typing import List, Optional
from pydantic import BaseModel, EmailStr

class Posts(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None
    
class Person(BaseModel):
    fname: str
    name:str
    age:int
    occupation:str

class Book(BaseModel):
    name: str
    descr: str
    pages: int
    amount: int
    tax: float | None = None
    
class Good(BaseModel):
    name: str
    descr: str
    price: float
    tax: Optional[float] = None
    tags: Optional[List[str]] = None
    
    
class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    fullname: str | None=None