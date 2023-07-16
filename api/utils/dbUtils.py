import databases
import sqlalchemy
from functools import lru_cache
# from api import config
from api.models import metadata
from starlette.config import Config

# @lru_cache
# def settings():
#     return config.Settings()

# # using pydantic to load .env file 
# def database_pgsql_url_config():
#     return str(settings().DB_CONNECTION+"://"+settings().DB_USERNAME+":"+settings().DB_PASSWORD+
#                "@"+settings().DB_HOST+":"+settings().DB_PORT+"/"+settings().DB_DATABASE)

#using starlette conf

def database_pgsql_url_config():
    conf=Config(".env")

    return str(conf("DB_CONNECTION")+"://"+conf("DB_USERNAME")+":"+conf("DB_PASSWORD")+
               "@"+conf("DB_HOST")+":"+conf("DB_PORT")+"/"+conf("DB_DATABASE"))

database=databases.Database(database_pgsql_url_config())
engine=sqlalchemy.create_engine(database_pgsql_url_config())
metadata.create_all(engine)