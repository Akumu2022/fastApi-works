from fastapi import Body, FastAPI
from models import Posts, Person
from random import randrange

app = FastAPI()

my_posts = [{"title":"I am Akumu Wycliff", "content":"The myth the mystery","id":"1"},
            {"title":"EPL today", "content":"Table Standings","id":"2"}]

fake_db = []

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

@app.post("/person")
async def add_person(person: Person):
    person_data = person.dict()
    fake_db.append(person_data)
    return{"data":person_data}




