from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access secrets
FLASK_SECRET_KEY = os.getenv("FLASK_SECRET_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT")