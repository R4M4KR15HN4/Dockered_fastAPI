from fastapi import APIRouter,Depends,HTTPException
from api.auth.schema import UserCreate,UserList
from api.auth import crud,schema
from api.utils import cryptUtils,jwtUtils,constantsUtil
from fastapi.security import OAuth2PasswordRequestForm




router=APIRouter(prefix="/api/v1")

@router.post("/auth/register",response_model=UserList)
async def register(user: UserCreate):

    #check user exits or not
    result=await crud.find_exist_user(user.email)
    if result:
        raise HTTPException(status_code=404,detail="User already exists")
    user.password = await cryptUtils.hash_passsword(user.password)
    
    #save new user
    await crud.save_user(user)

    return {**user.model_dump()}


@router.post("/auth/login")
async def login(form_data: OAuth2PasswordRequestForm=Depends()):
    result=await crud.find_exist_user(form_data.username)
    if not result:
        raise HTTPException(status_code=404,detail="User not found")

    #verify password
    user=schema.UserCreate(**result)
    verified_password=await cryptUtils.verify_password(form_data.password,user.password)

    if not verified_password:
        raise HTTPException(status_code=404,detail="Incorrect username or password")
    
    #create token
    acces_token_expires=jwtUtils.timedelta(minutes=constantsUtil.ACCESS_TOKEN_EXPIRE_MINUTE)
    access_token=await jwtUtils.create_access_token(
        data={"sub":form_data.username},
        expires_delta=acces_token_expires
    )




    return {"acccess_token":access_token,
            "token_type":"bearer",
            "user_info":{
                "email":user.email,
                "fullname":user.fullname
            }}