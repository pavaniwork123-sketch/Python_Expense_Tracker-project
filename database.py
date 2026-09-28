from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker 
Base=declarative_base()
url="mysql+mysqlconnector://root:Pavani%40123@localhost:3306/expenses"
engine=create_engine(url)
LocalSession=sessionmaker(bind=engine,autoflush=True)