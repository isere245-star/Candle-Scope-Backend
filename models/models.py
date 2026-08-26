from database.database import Base, engine
from sqlalchemy import Column, Integer, String

# Define the User model
class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=False, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    password = Column(String(100), nullable=False)

# Define database models here
Base.metadata.create_all(bind=engine)
