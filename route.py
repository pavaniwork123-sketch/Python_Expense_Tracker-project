from fastapi import FastAPI
from pydantic import BaseModel
from models import *
from database import LocalSession,Base,engine
from sqlalchemy import func

app=FastAPI()
Base.metadata.create_all(bind=engine)

class User(BaseModel):
    user_id:int
    user_name:str
class Expense(BaseModel):
    user_id:int
    expense_name:str
    expense_category:str
    expense_amount:int


@app.post("/add-expense")
def add_expense(request:Expense):
    db=LocalSession()
    expense=Expenses(
        user_id=request.user_id,
        expense_name=request.expense_name,
        expense_category=request.expense_category,
        expense_amount=request.expense_amount
    )
    db.add(expense)
    db.commit()
    db.close()
    return "Expense Added successfully"
@app.get("/showexpenses")
def show_expenses(user_id:int):
    db=LocalSession()
    expenses=db.query(Expenses).filter(Expenses.user_id==user_id).all()
    if not expenses:
        return "No expenses added "
    return expenses
class search(BaseModel):
    expense_category:str
    user_id:int
@app.get("/searchbycategory")
def search(expense_category:str,user_id:int):
    db=LocalSession()
    exp_cat=db.query(Expenses).filter(Expenses.expense_category==expense_category,
        Expenses.user_id==user_id).all()
    if not exp_cat:
        return "No expenses in this category"
    return exp_cat

@app.get("/filterbyamount")
def filter_amount(amount:int):
    db=LocalSession()
    expenses=db.query(Expenses).filter(Expenses.expense_amount>=amount).all()
    if not expenses:
        return "No expenses above this amount"
    return expenses
@app.get("/Totalexpenses")
def total_expenses(user_id:int):
    db=LocalSession()
    total=db.query(func.sum(Expenses.expense_amount)).filter(Expenses.user_id==user_id).scalar()
    if not total:
        return f"No expense by the User with {user_id}"
    return total
@app.get("/showinghighestexpense")
def show_highest(user_id:int):
    db=LocalSession()
    highest=db.query(func.max(Expenses.expense_amount)).filter(Expenses.user_id==user_id).scalar()
    return highest
@app.get("/show_all_Users")
def show_users():
    db=LocalSession()
    users_data=db.query(users).all()
    if not users_data:
        return "No active Users"
    else:
        return users_data
@app.delete("/deleteExpense")
def delete_expense(expense_id:int):
    db=LocalSession()
    expense=db.query(Expenses).filter(Expenses.Expense_id==expense_id).first()
    if not expense:
        db.close()
        return "No such expense exists"
    else:
        db.delete(expense)
        db.commit()
        db.close()
        return f"Expense {expense.expense_name} deleted successfully"
@app.post("/create_new_user")
def create_user(request:User):
    db=LocalSession()
    user=users(user_id=request.user_id,
               user_name=request.user_name)
    db.add(user)
    db.commit()
    db.close()
    return "User added successfully"