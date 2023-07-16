from sqlalchemy import Table,Column,Integer,String,DateTime,MetaData,Sequence

metadata=MetaData()
table_name="py_users"

users=Table(
    table_name,
    metadata,
    Column("id",Integer,Sequence("user_id_seq"),primary_key=True),
    Column("email",String(100)),
    Column("password",String(100)),
    Column("fullname",String(100)),
    Column("created_on",DateTime),
    Column("status",String(1))
)
   

