from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

### python3 -m pip install sqlalchemy
# SQLALCHEMY_DAATABASE_URL = "sqlite:///./todos.db"

# engine = create_engine(
#     SQLALCHEMY_DAATABASE_URL, connect_args={"check_same_thread": False}
# )

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()

## python3 -m pip install psycopg2-binary
# SQLALCHEMY_DAATABASE_URL = "postgresql://libintom:password123@localhost/bmt_bkend_db_1"
#SQLALCHEMY_DAATABASE_URL = "postgresql://libintom:password123@bmt-db-1.ce0njtqyahax.us-east-1.rds.amazonaws.com/bmtbkenddb1"
# SQLALCHEMY_DAATABASE_URL = "postgresql://postgres:password123@localhost/bmtbkenddb1"
# POSTGRES_USER = os.environ['POSTGRES_USER']
SQLALCHEMY_DAATABASE_URL = f"postgresql://{os.environ['POSTGRES_USER']}:{os.environ['POSTGRES_PASSWORD']}@{os.environ['POSTGRES_HOST']}/{os.environ['POSTGRES_DB']}"

engine = create_engine(SQLALCHEMY_DAATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

### python3 -m pip install pymysql

# SQLALCHEMY_DAATABASE_URL = "mysql+pymysql://root:popopo123@127.0.0.1:3306/todo_app_db1"

# engine = create_engine(SQLALCHEMY_DAATABASE_URL)

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()