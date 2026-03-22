# Import router and dependency tools
from fastapi import APIRouter, Depends

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
def register_user(user: UserRegister):
    print("\n📥 Register API called")

    # Create user
    created_user = create_user(user.email, user.password)

    print("✅ User registered successfully")

    return {
        "message": "User created successfully",
        "user": created_user
    }


# ================= LOGIN =================
# Import OAuth2 form
from fastapi.security import OAuth2PasswordRequestForm

# Import Depends
from fastapi import Depends


@router.post("/users/login")
def login_user(form_data: OAuth2PasswordRequestForm = Depends()):
    print("\n📥 Login API called (OAuth2 format)")

    # Extract email from "username" field
    email = form_data.username
    password = form_data.password

    print(f"👉 Received login request for: {email}")

    # Find user
    db_user = get_user_by_email(email)

    if not db_user:
        print("❌ User not found")
        return {"error": "User not found"}

    # Verify password
    if not verify_password(password, db_user["password"]):
        print("❌ Invalid password")
        return {"error": "Invalid password"}

    # Generate token
    token = create_access_token({"sub": email})

    print("✅ Login successful")

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