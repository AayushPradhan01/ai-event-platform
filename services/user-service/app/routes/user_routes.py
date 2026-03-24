# Import router and dependency tools
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db

# Import schemas
from app.schemas.user_schema import UserRegister, UserLogin

# Import service functions
from app.services.user_service import (
    create_user,
    get_user_by_email,
    verify_password,
    create_access_token
)

# Import authentication dependency
from app.services.auth_service import get_current_user

# Create router object
router = APIRouter()


# ================= REGISTER =================
@router.post("/users/register")
def register_user(user: UserRegister, db: Session = Depends(get_db)):
    print("\n📥 Register API called")

    created_user = create_user(db, user.email, user.password)

    if not created_user:
        return {
            "success": False,
            "message": "Email already registered"
    }

    return {
        "success": True,
        "message": "User created successfully",
        "user_email": created_user.email
    }


# ================= LOGIN =================
# Import OAuth2 form
from fastapi.security import OAuth2PasswordRequestForm

# Import Depends
from fastapi import Depends


@router.post("/users/login")
def login_user(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    print("\n📥 Login API called")

    email = form_data.username
    password = form_data.password

    db_user = get_user_by_email(db, email)

    if not db_user:
        return {"success": False, "message": "User not found"}

    if not verify_password(password, db_user.password):
        return {"success": False, "message": "Invalid password"}

    token = create_access_token({"sub": email})

    return {
        "access_token": token,
        "token_type": "bearer"
    }


# ================= PROTECTED ROUTE =================
@router.get("/users/me")
def get_current_user_route(current_user: str = Depends(get_current_user)):
    print("\n📥 /users/me API called")

    # current_user comes from token automatically
    print("✅ Authenticated user:", current_user)

    return {
        "message": "User authenticated successfully",
        "user_email": current_user
    }