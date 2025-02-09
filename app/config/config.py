import os
from dotenv import load_dotenv

load_dotenv()

API_USERS_URL = os.getenv("API_USERS_URL", "https://jsonplaceholder.typicode.com/users")