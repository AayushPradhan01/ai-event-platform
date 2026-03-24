from sqlalchemy.exc import IntegrityError

# Import password hashing
from passlib.context import CryptContext

# Import DB session
from sqlalchemy.orm import Session

# Import User model
from app.models.user_model import User

# JWT imports
from jose import jwt
from datetime import datetime, timedelta


# =========================
# PASSWORD HASHING SETUP
# =========================
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# =========================
# HASH PASSWORD
# =========================
def hash_password(password: str):
    print("🔐 Hashing password...")

    # bcrypt limitation
    password = password[:72]

    return pwd_context.hash(password)


# =========================
# CREATE USER (DB INSERT)
# =========================
def create_user(db: Session, email: str, password: str):
    print("👤 Creating user in database...")

    # 🔍 Check if user already exists
    existing_user = db.query(User).filter(User.email == email).first()

    if existing_user:
        print("❌ Email already registered")

        # Return clean error instead of crashing
        return None

    # Hash password
    hashed_password = hash_password(password)

    # Create user object
    new_user = User(
        email=email,
        password=hashed_password
    )

    try:
        # Add to DB
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        print("✅ User saved in database")

        return new_user

    except IntegrityError:
        # Rollback in case of DB failure
        db.rollback()

        print("❌ Database error occurred")

        return None


# =========================
# GET USER BY EMAIL
# =========================
def get_user_by_email(db: Session, email: str):
    print("🔍 Fetching user from DB...")

    return db.query(User).filter(User.email == email).first()


# =========================
# VERIFY PASSWORD
# =========================
def verify_password(plain_password: str, hashed_password: str):
    print("🔍 Verifying password...")

    return pwd_context.verify(plain_password[:72], hashed_password)


# =========================
# JWT CONFIG
# =========================
SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


# =========================
# CREATE TOKEN
# =========================
def create_access_token(data: dict):
    print("🎟️ Generating JWT token...")

    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)