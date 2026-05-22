from pydantic import BaseModel
from fastapi import APIRouter

router = APIRouter()

class RegisterUser(BaseModel):
    fname: str
    lname: str
    password: str
    email: str
    contact: str

@router.post("/register")
def register_user(user: RegisterUser):

    if len(user.password) < 8:
        return {
            "status": "Registration Failed",
            "message": "Password must be at least 8 characters"
        }

    return {
        "status": "Success",
        "message": "User registered successfully",
        "user": {
            "firstname": user.fname,
            "lastname": user.lname,
            "email": user.email,
            "contact": user.contact
        }
    }