users = {

}

print("Choose an Option")

while True:
    choose = input("Log In or Sign Up: ").title()

    if choose == "Sign Up":
        entered_username_sign_up = input("Please Enter Your Username: ")
        entered_password_sign_up = input("Please Enter Your Password: ")
        users[entered_username_sign_up] = entered_password_sign_up
        print("Your Account's Information: ", users)

    elif choose == "Log In":
        entered_username_log_in = input("Please Enter Your Username: ")
        entered_password_log_in = input("Please Enter Your Password: ")
        if entered_username_log_in not in users or users[entered_username_log_in] != entered_password_log_in:
            print("Please Sign Up First")
        else:
            print("Your Account's Information: ", users)
        
            break