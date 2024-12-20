from user_signup import register, login, password_recovery

def main():
    while True:
        choice = input("Choose an option: register / login / recovery / quit: ").lower()
        if choice == "register":
            register()
        elif choice == "login":
            login()
        elif choice == "recovery":
            password_recovery()
        elif choice == "quit":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

main()