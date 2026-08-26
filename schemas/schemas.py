from pydantic import BaseModel

# Define Pydantic models for data validation
class User(BaseModel):
    id: int
    username: str
    email: str
    password: str

    # Config class to enable ORM mode for Pydantic models
    class Config:
        orm_mode = True