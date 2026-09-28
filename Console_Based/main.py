from expense_function import add_expense,view_expenses,search_by_category,show_highest,show_total,create_user,filter_by_amount,show_users
print(f"{'-'*15}{'Welcome to the Expense Tracker'}{'-'*15}")
print("\n1.Create a new user \n2.Add expense\n3.View expenses \n4.Search by Category \n5.Filter expenses by Amount\n6.Show total\n7.Show highest expense\n8.Show all Users\nEnter '0' to exit")

while True:
    choice=input("\nSelect your choice: ")
    if choice=='1':
        create_user()
    elif choice=='2':
        add_expense()
    elif choice=='3':
        view_expenses()
    elif choice=='4':
        search_by_category()
    elif choice=='5':
        filter_by_amount()
    elif choice=='6':
        show_total()
    elif choice=='7':
        show_highest()
    elif choice=='0':
        break
    elif choice=='8':
        show_users()
    else:
        print("Enter Valid Choice!!!!!")
