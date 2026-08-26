from database.database import *
from models.models import *
from auth.auth import *

Session = Session()

# Function to get a database session
def get_db():

    db = Session
    try:
        yield db
    finally:
        db.close()

# Function to create a new user in the database
def create_user(user: User):
    
    # Create a new User instance with hashed password
    User_add = User( 
        username = user.username, 
        email = user.email,
        password = hash_password(user.password))

    # Check if the email already exists in the database
    Verify_email = Session.query(User).filter(User.email == user.email).first()

    # If the email does not exist, add the new user to the database
    if not Verify_email :
        # Add the new user to the database
        Session.add(User_add)
        Session.commit()
        Session.refresh(User_add)
        return User_add