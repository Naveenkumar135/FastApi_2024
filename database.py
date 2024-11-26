from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# MySQL Database URL (change this to your actual MySQL database credentials)
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:tl%40123456@localhost/test_db"

# Create the database engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for ORM models
Base = declarative_base()

def get_db():
    db = SessionLocal()  # Open a session
    try:
        yield db  # Provide session to route function
    finally:
        db.close()  # Ensure session is closed after request
