import time

print("Please insert your CARD")
time.sleep(2)

PASSWORD = 1234
balance = 5000
transactions = []

pin = int(input("Enter your ATM PIN: "))

if pin == PASSWORD:
    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Transaction History")
        print("5. Exit")
        print("====================")

        try:
            option = int(input("Please enter your choice: "))
        except:
            print("Invalid input! Please enter a number.")
            continue

        # ✅ Check Balance
        if option == 1:
            print(f"Your current balance is ₹{balance}")

        # ✅ Withdraw
        elif option == 2:
            withdraw_amount = int(input("Enter amount to withdraw: "))

            if withdraw_amount > balance:
                print("Insufficient balance!")
            elif withdraw_amount <= 0:
                print("Enter valid amount!")
            else:
                balance -= withdraw_amount
                print(f"₹{withdraw_amount} debited from your account")
                print(f"Updated balance: ₹{balance}")

                # Transaction record
                transactions.append(f"Withdraw: ₹{withdraw_amount}, Balance: ₹{balance}")

        # ✅ Deposit
        elif option == 3:
            deposit_amount = int(input("Enter amount to deposit: "))

            if deposit_amount <= 0:
                print("Enter valid amount!")
            else:
                balance += deposit_amount
                print(f"₹{deposit_amount} credited to your account")
                print(f"Updated balance: ₹{balance}")

                # Transaction record
                transactions.append(f"Deposit: ₹{deposit_amount}, Balance: ₹{balance}")

        # ✅ Transaction History
        elif option == 4:
            print("\n----- Transaction History -----")
            if not transactions:
                print("No transactions yet.")
            else:
                for t in transactions:
                    print(t)

        # ✅ Exit
        elif option == 5:
            print("Thank you for using ATM. Goodbye!")
            break

        else:
            print("Please select a valid option!")

else:
    print("Wrong PIN! Access denied.")