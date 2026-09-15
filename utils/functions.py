
import os

def get_env_var(var_name):
    """
    Function to retrieve the value of an environment variable.

    Args:
        var_name (str): The name of the environment variable to retrieve.

    Returns:
        str: The value of the environment variable, or None if not found.
    """
    return os.environ.get(var_name)
