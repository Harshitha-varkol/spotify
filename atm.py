# Simple ATM Balance Checker with hardcoded values

# Hardcoded account details
account_number = "1234567890"
pin = "1234"
balance = 5000.00

print("=" * 40)
print("      WELCOME TO ABC BANK ATM")
print("=" * 40)

# Get user input
input_account = input("\nEnter Account Number: ")
input_pin = input("Enter PIN: ")

# Verify account details
if input_account == account_number and input_pin == pin:
    print("\n✓ Authentication Successful!")
    print("-" * 40)
    print(f"Account Number: {account_number}")
    print(f"Current Balance: ${balance:.2f}")
    print("-" * 40)
    print("\nThank you for using ABC Bank ATM!")
else:
    print("\n✗ Invalid Account Number or PIN!")
    print("Access Denied.")

print("=" * 40)