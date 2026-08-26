from pydantic import BaseModel

# Define Pydantic models for data validation
class User_create (BaseModel):
    username: str
    email: str
    password: str

    # Config class to enable ORM mode for Pydantic models
    class Config:
        from_attributes = True