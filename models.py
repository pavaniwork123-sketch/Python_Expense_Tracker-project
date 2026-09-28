from database import Base
from sqlalchemy import Column,ForeignKey,Integer,String
class users(Base):
    __tablename__="Users_Expense"
    user_id=Column(Integer,primary_key=True,autoincrement=True)
    user_name=Column(String(50),nullable=False)

class Expenses(Base):
    __tablename__="Expense_data"
    Expense_id=Column(Integer,primary_key=True,autoincrement=True)
    user_id=Column(Integer,ForeignKey("Users_Expense.user_id"))
    expense_name=Column(String(100),nullable=False)
    expense_category=Column(String(100),nullable=False)
    expense_amount=Column(Integer,nullable=False)


