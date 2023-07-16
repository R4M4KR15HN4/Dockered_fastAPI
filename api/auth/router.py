from fastapi import APIRouter,Depends,HTTPException
from api.auth.schema import UserCreate
from api.auth import crud 
from api.utils import cryptUtils

router=APIRouter()

@router.post("/auth/register")
async def register(user: UserCreate):

    #check user exits or not
    result=await crud.find_exist_user(user.email)

    if result:
        raise HTTPException(status_code=404,detail="User already exists")
    print(f'#.20')
    print(user.password)
    
    user.password = cryptUtils.hash_passsword(user.password)
    
    #save new user
    await crud.save_user(user)

    return {**user.model_dump()}