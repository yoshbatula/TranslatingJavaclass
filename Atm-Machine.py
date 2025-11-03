from Account import Account

class ATM:

    if __name__ == "__main__":

        account = Account(0)

        while True:
            print("\nATM Machine Simulation")
            print("[1]: Check Balance")
            print("[2]: Deposit Money")
            print("[3]: Withdraw Money")
            print("[4]: Exit")

            choice = input("Select an option: ")

            if choice == '1':
                account.check_balance()
            elif choice == '2':
                amount = float(input("Enter the amount to deposit: "))
                account.deposit(amount)
            elif choice == '3':
                amount = float(input("Enter the amount to withdraw: "))
                account.withdraw(amount)
            elif choice == '4':
                print("Exiting...")
                break  
            else:
                print("Invalid option selected.")
