# import uuid
from csv import unregister_dialect
import uuid

# import typing list    
from typing import List

# import FastAPI and HTTPException
from fastapi import FastAPI, HTTPException

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
                   
                    User(
                    # doesn't work with uuid.uuid4()
                    # id= uuid("3ed2f813-9f91-4942-823a-fddcadbdf518"),
                    # not sure how to pass my own id!
                    first_name= "KJ", 
                    last_name="Doey", 
                    middle_name="Smithy",
                    email="aagoodboy@gmail.com",
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

# create a put route to update a user
@app.put("/api/v1/users/{user_id}")
async def update_user(user: User):
    # get the user from the db
    # loop through the db
    for user in db:
        if user.id == user_id:

            if user_to_update.first_name is not None:
                user.first_name = user_to_update.first_name

            if user_to_update.last_name is not None:
                user.last_name = user_to_update.last_name
                 
            if user_to_update.middle_name is not None:
                user.middle_name = user_to_update.middle_name

            if user_to_update.email is not None:
                user.email = user_to_update.email

            if user_to_update.status is not None:
                user.status = user_to_update.status
            if user_to_update.role is not None:
                user.role = user_to_update.role
            return 

    raise HTTPException(status_code=404, detail=f"User{user}not found")


# delete a user
@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: uuid.UUID):
    # loop through the db
    for user in db:
        # check if the user id is the same as the user_id
        if user.id == user_id:
            # remove the user from the db
            db.remove(user)
            # return the user id
            return {"id": user_id}
    # if the user id is not found raise an HTTPException with a 404 status code
    # and a message specifying which user was not found 
    raise HTTPException(status_code=404, 
                        detail=f"User with id {user_id} not found")
    