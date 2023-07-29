from api.utils.dbUtils import database
from api.auth.schema import UserCreate


def find_exist_user(email: str):
    query: str = "select * from py_users where status='1' and email=:email"

    return database.fetch_one(query, values={"email": email})





def save_user(user: UserCreate):
    query: str = """insert into py_users Values(nextval('user_id_seq'),:email,:password,:fullname,now() at time zone 'UTC','1')"""
    return database.execute(query,values={"email":user.email,"password":user.password,"fullname":user.fullname})
