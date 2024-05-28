from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///sql_app.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)

Base = declarative_base()
sess_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db_conn = sess_local()
