import jwt
from api.utils import constantsUtil

from datetime import datetime,timedelta

async def create_access_token(*,data: dict,expires_delta: timedelta=None):
    to_encode=data.copy()
    if expires_delta:
        expire=datetime.utcnow()+expires_delta
    else:
        expire=datetime.utcnow()+timedelta(minutes=constantsUtil.ACCESS_TOKEN_EXPIRE_MINUTE)
    to_encode.update({'exp':expire})
    return jwt.encode(to_encode,constantsUtil.SECRET_KEY,algorithm=constantsUtil.ALGORITHM_HS256)


