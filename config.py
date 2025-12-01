import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Database URL
DATABASE_URL = os.environ.get('DATABASE_URL', 'postgresql://postgres:567234@localhost:5432/postgres')

# Create engine
engine = create_engine(DATABASE_URL, echo=False)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create base class for models
Base = declarative_base()


def get_session():
    """Get database session"""
    session = SessionLocal()
    try:
        return session
    except Exception as e:
        session.close()
        raise e
