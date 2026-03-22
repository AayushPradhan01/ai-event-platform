# Import password hashing library
from passlib.context import CryptContext

# Create password hashing context
# bcrypt is industry standard hashing algorithm
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# Fake database (temporary)
# This is just a Python list storing users
fake_users_db = []


# Function to hash password
def hash_password(password: str):
    print("🔐 Hashing password...")

    # bcrypt only supports 72 characters → truncate
    password = password[:72]

    # Return hashed password
    return pwd_context.hash(password)


# Function to create new user
def create_user(email: str, password: str):
    print("👤 Creating user...")

    # Hash password before storing
    hashed_password = hash_password(password)

    # Create user object (dictionary)
    user = {
        "email": email,
        "password": hashed_password
    }

    # Save user to fake DB
    fake_users_db.append(user)

    print("✅ User stored in database")

    return user


# Function to verify password during login
def verify_password(plain_password: str, hashed_password: str):
    print("🔍 Verifying password...")

    # Compare plain password with hashed password
    return pwd_context.verify(plain_password[:72], hashed_password)


# Function to find user by email
def get_user_by_email(email: str):
    print("🔍 Searching user in database...")

    # Loop through fake DB
    for user in fake_users_db:
        if user["email"] == email:
            print("✅ User found")
            return user

    print("❌ User not found")
    return None


# ================= JWT PART =================

# Import JWT library
from jose import jwt

# Import time utilities
from datetime import datetime, timedelta

# Secret key (used to sign token)
SECRET_KEY = "mysecretkey"

# Algorithm used for JWT
ALGORITHM = "HS256"

# Token expiry time
ACCESS_TOKEN_EXPIRE_MINUTES = 30


# Function to create JWT token
def create_access_token(data: dict):
    print("🎟️ Generating JWT token...")

    # Copy data to avoid modifying original
    to_encode = data.copy()

    # Set token expiry time
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    # Add expiry to token payload
    to_encode.update({"exp": expire})

    # Encode token
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    print("✅ Token created successfully")

    return encoded_jwt