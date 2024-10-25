import sqlite3
from dbase import *

# Authorized user (this can be fetched from a database or list)
AUTHORIZED_USER_ID = '123456789'  # Replace with actual authorized user's Telegram ID

def main():
    adminid = input("Enter telegram userid to be made admin: ")
    
    # Check if the person running the script is authorized
    current_user = input("Enter your telegram user ID to authorize: ")
    
    if current_user != AUTHORIZED_USER_ID:
        print("Unauthorized! Only the main admin can add new admins.")
        return
    
    check = check_admin(adminid)
    if check:
        print("Admin already exists")
    else:
        try:
            create_admin(adminid)
            create_user_lifetime(adminid)
        except Exception as e:
            print(f"Something went wrong: {e}")
        else:
            print(f"Admin with ID {adminid} created successfully.")

if __name__ == '__main__':
    main()
