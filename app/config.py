import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DEBUG = os.environ.get("DEBUG", "False").lower() == "true"
    TESTING = os.environ.get("TESTING", "False").lower() == "true"

    SECRET_KEY = os.environ.get("SECRET_KEY")
    if not SECRET_KEY:
        raise ValueError("No SECRET_KEY set for Flask application. Set it in the environment or .env file.")

