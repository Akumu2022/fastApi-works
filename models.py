from typing import List, Optional
from pydantic import BaseModel, EmailStr
from uuid import UUID, uuid4
from enum import Enum

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


# day 2 practice
# advancing to more complex apis
class Gender(str, Enum):
    male = "male"
    female = "female"
    
class Role(str, Enum):
    admin = "admin"
    user = "user"
    student = "student"

class User(BaseModel):
    id: Optional [UUID] = uuid4()
    firstName:Optional [UUID] = uuid4()
    lastName: str
    # middleName: str | None = None
    middleName: Optional[str] = None
    gender: Gender
    roles:List[Role]
