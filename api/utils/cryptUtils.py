from passlib.context import CryptContext


password_context=CryptContext(schemes=["bcrypt"])

async def hash_passsword(password: str):
    return password_context.hash(password_context)

async def verify_hash(plain_password: str,hashed_password: str):
    return password_context.verify(plain_password,hashed_password)

