# Import SQLAlchemy column types
from sqlalchemy import Column, Integer, String

# Import Base class
from app.database.database import Base


# =========================
# USER TABLE
# =========================

class User(Base):
    # Table name in database
    __tablename__ = "users"

    # Primary key (auto increment ID)
    id = Column(Integer, primary_key=True, index=True)

    # Email column (unique)
    email = Column(String(255), unique=True, index=True)

    # Password column
    password = Column(String)