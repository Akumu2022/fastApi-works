import statistics
from fastapi import Body, FastAPI, HTTPException, Query
from models import Posts, Person, Book, Good, UserIn
from random import randrange
from typing import Optional
from pydantic import BaseModel


app = FastAPI()

my_posts = [{"title":"I am Akumu Wycliff", "content":"The myth the mystery","id":"1"},
            {"title":"EPL today", "content":"Table Standings","id":"2"}]

db = [{"fname":"Akumu","name":"Wycliff", "age":111,"occupation":"player"}]


fake_db = [Person]

@app.get("/posts")
async def get_post():
    return {"data":my_posts}

@app.post("/posts")
def create_posts(post: Posts):
    post_dict = post.model_dump()
    post_dict['id'] = randrange(0,100000000)
    my_posts.append(post_dict)
    return {"data":post_dict}

@app.get("/posts/{id}")
def get_user(id):
    return{"data":f"this is it {id}"}


@app.post("/post")
async def add_new_user(person:Person):
    dict_data = person.model_dump()
    return{"data":dict_data,"msg":"user added successfully"}

@app.get("/post")
async def get_added_user(person:Person):
    return{"data":person,"message":"successs"}

@app.get("/items")
async def list_items():
    return{"msg":"these are the items routes"}

@app.get("/items/{item_id}")
async def get_items(item_id: int):
    return{"item ID":item_id}

fake_items_db = [{"item_name":"Foo","item_name":"xyz","item_name":"efg",}]

@app.get("/itemz")
async def get_items(skip:int = 0, limit:int =10):
    return fake_items_db[skip: skip+limit]

@app.get("/users/{user_id}")
async def get_them_users(user_id: int, q:str |None = None):
    if q:
        return{"user ID":user_id, "query":q}
    return{"user ID":user_id}

@app.post("/books")
async def add_new_book(book:Book,
                       discount: float = Query(default=None,description="Discount applied to the book price")
                       ):
    user_dict = book.model_dump()
    if book.tax:
        price_with_tax = book.tax + book.amount
        user_dict.update({"price_with_tax":price_with_tax})
    return{"data":user_dict, "msg":"added successfully"}

@app.post("/goods/")
async def add_goods(goods: Good):
    return goods

@app.post("/user/", response_model= UserIn)
async def create_user(user:UserIn):
    return user