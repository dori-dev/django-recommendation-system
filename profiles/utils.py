"""profiles utils
"""
from django.utils.crypto import get_random_string


def generate_code() -> str:
    """generate the recommendation code

    Returns:
        str: random recommendation code
    """
    code = get_random_string(12)
    return code
