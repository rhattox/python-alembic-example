from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)

# Replace 'your_database_url' with the actual database URL
engine = create_engine('postgresql://postgres:postgres@db:5432/python_database')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
