from db import create_connection
def add_expense():
    user_id=int(input("Enter your user ID: "))
    name=input("Give a name to this expense:")
    expense_name=name.strip().title()
    category=input("What is this expense about: ")
    expense_category=category.title().strip()
    expense_amount=int(input("Enter the expense amount: "))
    connection=create_connection()
    pen=connection.cursor()
    input_tuples=(user_id,expense_name,expense_category,expense_amount)
    query="INSERT INTO EXPENSES(user_id,expense_name,expense_category,expense_amount) VALUES (%s,%s,%s,%s);"
    pen.execute(query,input_tuples)
    print("Expense Added successfully!!!")
    connection.commit()
    pen.close()
    connection.close()

def view_expenses():
    connection=create_connection()
    pen=connection.cursor()
    user=int(input("Enter your user ID: "))
    query="Select * from EXPENSES Where User_id=%s;"
    pen.execute(query,user)
    result=pen.fetchall()
    print(f"\n\n{'='*30}Your expenses{'='*30}")
    print(f"{'Expense Name':<40}{'Expense Category':<40}{'Expense Amount':<20}")
    for i in result:
        print(f"{i[2]:<40}{i[3]:<40}{i[4]:<20}")
    print('='*75)


def search_by_category():
    category=input("\nEnter the category you want to print: ")
    user=int(input("Enter your UserID: "))
    connection=create_connection()
    pen=connection.cursor()
    query="Select * from EXPENSES WHERE expense_category=%s and user_id=%s;"
    pen.execute(query,(category,user))
    result=pen.fetchall()
    print('='*70)
    print(f"{'Expense Name':<40}{'Expense Category':<40}{'Expense Amount':<20}")
    for i in result:
        print(f"{i[2]:<40}{i[3]:<40}{i[4]:<40}") 
    print('='*70)

def filter_by_amount():
    Connection=create_connection()
    pen=Connection.cursor()
    user=int(input("Enter your user ID: "))
    print("\n")
    amount=int(input("Enter the amount to be filtered: "))
    query="Select * from EXPENSES where expense_amount>=%s and user_id=%s;"
    pen.execute(query,(amount,user))
    result=pen.fetchall()
    print('='*70)
    print(f"{'Expense Name':<40}{'Expense Category':<40}{'Expense Amount':<20}")
    for i in result:
        print(f"{i[2]:<40}{i[3]:<40}{i[4]:<20}") 
    print('='*70)

def show_total():
    connection=create_connection()
    pen=connection.cursor()
    user=int(input("Enter Your User Id To see your expenses: "))
    query="Select sum(expense_amount) from EXPENSES where user_id=%s;"
    pen.execute(query,user)
    result=pen.fetchone()
    print(f"\n{'='*30}{'Total Expense'}{'='*30}")
    print(f"Total amount Spent: {result[0]}")

def show_highest():
    connection=create_connection()
    pen=connection.cursor()
    user=int(input("Enter the user Id to see your highest expense: "))
    query="Select max(expense_amount) from EXPENSES where user_id=%s;"
    pen.execute(query,user)
    result=pen.fetchone()
    print(f"\n{'='*30}{'Higest Expense'}{'='*30}")
    print(f"Highest expense :{result[0]}")

def create_user():
    connection=create_connection()
    pen=connection.cursor()
    user_name=input("Enter the user name: ")
    query="Insert into USERS(user_name)values (%s);"
    pen.execute(query,user_name)
    query2="select user_id from USERS where user_name=%s;"
    pen.execute(query2,user_name)
    result2=pen.fetchone()
    print(f"Your User Id is: {result2[0]}\nUse this to add expenses")
    print("You are added to the Database")
    connection.commit()
    pen.close()
    connection.close()

def show_users():
    Connection=create_connection()
    pen=Connection.cursor()
    query="Select * from USERS;"
    pen.execute(query)
    result=pen.fetchall()
    print(f"{'='*30}{'USER DETAILS'}{'='*30}")
    print(" ")
    print(f"{'USERID':<40}{'USER NAME'}")
    for i in result:
        print(f"{i[0]:<40}{i[1]}")
    