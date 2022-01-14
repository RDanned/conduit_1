import bcrypt
from core.settings import settings


def hash_pass(password: str) -> str:
    return bcrypt.hashpw(bytes(password, encoding='utf8'), salt=bcrypt.gensalt()).decode('utf-8')
