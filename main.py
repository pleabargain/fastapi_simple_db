# import uuid
import uuid

# import typing list    
from typing import List

# import FastAPI
from fastapi import FastAPI

# import User, Status and Role from models.py
from models import User, Status, Role

# create an instance of FastAPI
app = FastAPI()

# create a simple list of users
# middle_name: Optional[str] = None
    # email: str
    # status: Status
    # role: list[Role]
    # NB: using https://github.com/tulios/json-viewer to view the json
    # TODO need to figure out how to use data from https://www.mockaroo.com/ to speed up API data creation
db: List[User] = [
                    User(
                    id = uuid.uuid4(),
                    first_name= "John", 
                    last_name="Doe", 
                    middle_name="Smith",
                    email="goodboy@gmail.com",
                    # status= ["active"]
                    status= Status.active,
                    role=[Role.admin],
                        ),

                    User(
                    id= uuid.uuid4(),
                    first_name= "Joane", 
                    last_name="Doe", 
                    middle_name="Smith",
                    email="agoodboy@gmail.com",
                    status= Status.active,
                    role=[Role.user],
                        ),
                   
                    
                ]


#create a Hello World route
@app.get("/")   
def root():
    #return a hello world dictionary
    return {"Hello": "World from FastAPI and anothter link here http://127.0.0.1:8000/api/v1/users"}
    # can't add a second return statement
    # return {"aHello": "World from FastAPI and anothter link here http://127.0.0.1:8000/api/v1/users"}

    # test the app by running in the terminal
    # uvicorn main:app --reload   


# create a route to get all users
@app.get("/api/v1/users")
#asnyc def get_users():
async def get_users():
    # return the list of users
    return db

# create a route to register a user
@app.post("/api/v1/users")
async def register_user(user: User):
    # add the user to the db
    db.append(user)
    # return the user with id
    return{"id": user.id}
