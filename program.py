from user_signup import register, login

def main():
    while True:
        choice = input("Choose an option: register / login / quit: ").lower()
        if choice == "register":
            register()
        elif choice == "login":
            login()
        elif choice == "quit":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

main()
