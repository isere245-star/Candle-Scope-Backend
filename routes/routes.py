from fastapi import FastAPI, Depends
from schemas.schemas import *
from services.services import *

app = FastAPI()

# Define the route for user inscription
@app.post("/inscription", response_model=User_create)
# Define the inscription endpoint that takes user information and creates a new user in the database
def inscription(user: User_create, db: Session = Depends(get_db)):
    return create_user(user)
