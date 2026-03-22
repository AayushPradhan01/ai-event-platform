# Import BaseModel for creating schemas (data validation)
# EmailStr validates proper email format
from pydantic import BaseModel, EmailStr


# Schema for user registration
class UserRegister(BaseModel):
    # Email must be valid email format
    email: EmailStr

    # Password is a string
    password: str


# Schema for user login
class UserLogin(BaseModel):
    # Email must be valid email format
    email: EmailStr

    # Password is a string
    password: str