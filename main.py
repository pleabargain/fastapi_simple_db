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
    return {"Hello": "World"}
    # test the app by running in the terminal
    # uvicorn main:app --reload   


# create a route to get all users
@app.get("/api/v1/users")
#asnyc def get_users():
async def get_users():
    # return the list of users
    return db