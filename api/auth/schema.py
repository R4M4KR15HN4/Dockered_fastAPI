from pydantic import BaseModel,Field

class UserCreate(BaseModel):

    email: str=Field(...,example="nasole@gmail.com")
    password: str=Field(...,example="axxs@Jol123")
    full_name: str=Field(...,example="nasole parker")