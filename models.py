"""
Models for fast api
"""


import enum
import uuid
from typing import List

from pydantic import BaseModel


class Gender(str, enum.Enum):
    male = "male",
    female = "female"


class Role(str, enum):
    admin = "admin",
    user = "user",
    student = "student"


class User(BaseModel):
    """
    User model
    """
    id: uuid.UUID = uuid.uuid4()
    first_name: str
    middle_name: str
    last_name: str
    gender: Gender
    roles: List[Role]

    class Config:
        anystr_strip_whitespace = False,
        allow_mutation = False,
