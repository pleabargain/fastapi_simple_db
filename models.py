import uuid 

# import pydantic

from pydantic import BaseModel
# import from typing optional and list
from typing import Optional, List
from enum import Enum

#create a class for status
class Status(str, Enum):
    active = "active"
    inactive = "inactive"

#create a class for role
class Role(str, Enum):
    admin = "admin"
    user = "user"
    student = "student"


# create a class for the user
class User(BaseModel):

    # create id with optional  UUID

    id: Optional[uuid.UUID] = uuid.uuid4()
    
    # create a class variable for the first_name
    first_name: str
    # create a class variable for the last_name
    last_name: str
    # create a class variable for the middle_name
    middle_name: Optional[str] = None
    # create a class variable for the email
    email: str
    status: Status
    role: list[Role]

# create a class for the user Update
class UserUpdate(BaseModel):
    # create a class variable for the first_name
    first_name: Optional[str] = None
    # create a class variable for the last_name
    last_name: Optional[str] = None
    # create a class variable for the middle_name
    middle_name: Optional[str] = None
    # create a class variable for the email
    email: Optional[str] = None
    status: Optional[Status] = None
    role: Optional[list[Role]] = None