from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    url = "postgresql://postgres:220901@localhost:5432/finance_manager_db"
)

session_local = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()