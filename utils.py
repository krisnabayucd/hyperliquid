from dotenv import load_dotenv
import os

load_dotenv()

def get_config():
    address = os.getenv("ACCOUNT_ADDRESS")
    secret = os.getenv("SECRET")
    base_url = os.getenv("BASE_URL")
    if not all([address, secret, base_url]):
        raise ValueError("Missing required environment variables: ADDRESS, SECRET, BASE_URL")
    
    return address, secret, base_url

