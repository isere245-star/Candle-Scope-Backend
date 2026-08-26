from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Initialize the database engine and session
engine = create_engine("mysql://root:@localhost/base", echo=True, future=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
