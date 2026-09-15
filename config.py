from dotenv import load_dotenv

from utils.functions import get_env_var

# Load environment variables from .env file
load_dotenv(override=True)

config = {
    "WATSONX_PROJECT_ID": get_env_var("WATSONX_PROJECT_ID"),
    "WATSONX_API_KEY": get_env_var("WATSONX_API_KEY"),
    "WATSONX_URL": get_env_var("WATSONX_URL")
}
