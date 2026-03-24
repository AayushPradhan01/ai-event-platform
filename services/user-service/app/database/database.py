# Import SQLAlchemy engine creator
from sqlalchemy import create_engine

# Import session maker (used to talk to DB)
from sqlalchemy.orm import sessionmaker

# Import base class for models
from sqlalchemy.ext.declarative import declarative_base


# =========================
# DATABASE CONNECTION STRING
# =========================

# This is SQL Server connection string
# Update server name if needed
DATABASE_URL = "mssql+pyodbc://@localhost/EventDB?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"


# =========================
# CREATE ENGINE
# =========================

# Engine = connection between Python and DB
engine = create_engine(DATABASE_URL)


# =========================
# SESSION (DB OPERATIONS)
# =========================

# SessionLocal will be used to perform DB operations
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# =========================
# BASE CLASS FOR MODELS
# =========================

# All tables will inherit from this
Base = declarative_base()


# =========================
# GET DB SESSION (Dependency)
# =========================

# This function will give a DB session to our APIs
def get_db():
    # Create a new database session
    db = SessionLocal()

    try:
        # Provide the session to the API
        yield db

    finally:
        # Close the session after request is complete
        db.close()