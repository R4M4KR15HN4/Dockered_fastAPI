from passlib.context import CryptContext


pwd_context=CryptContext(schemes=["bcrypt"])

async def hash_passsword(password: str):
    return pwd_context.hash(password)

async def verify_password(plain_password: str,hashed_password: str):
    return pwd_context.verify(plain_password,hashed_password)

