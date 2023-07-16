# User Authentication
def validateCredentials(username, password):
    # Val.idate username and password against database or authentication system
    # Return True if valid, False otherwise
    # Implement your own validation logic here
    valid_username = "admin"
    valid_password = "password123"
    return username == valid_username and password == valid_password

# Transaction Processing
def processDeposit(accountNumber, amount):
    # Process the deposit transaction
    # Perform necessary validation and database operations
    # Implement your own deposit logic here
    print("Processing deposit of {amount} into account {accountNumber}")

def processWithdrawal(accountNumber, amount):
    # Process the withdrawal transaction
    # Perform necessary validation and database operations
    # Implement your own withdrawal logic here
    print("Processing withdrawal of {amount} from account {accountNumber}")

def processBalanceInquiry(accountNumber):
    # Perform a balance inquiry for the given account
    # Retrieve and display the account balance
    # Implement your own balance inquiry logic here
    balance = 1000  # Replace with actual balance retrieval from the database
    print("Account {accountNumber} balance: {balance}")

# User Interface
def displayLoginPage():
    # Display the login page UI elements
    print(" Login Page ")

def displayErrorMessage(message):
    # Display an error message to the user
    print("Error: {message}")

def readInput(prompt):
    # Display the prompt and read user input
    return input(prompt)

def displayMenu():
    # Display the main menu UI elements
    print(" Main Menu ")
    print("1. Deposit")
    print("2. Withdrawal")
    print("3. Balance Inquiry")
    print("4. Exit")

# Main program flow
username = ""
password = ""
authenticated = False

while not authenticated:
    displayLoginPage()
    username = readInput("Enter username: ")
    password = readInput("Enter password: ")

    if validateCredentials(username, password):
        authenticated = True
    else:
        displayErrorMessage("Invalid username or password. Please try again.")

transactionType = ""
accountNumber = ""
amount = 0.0

displayMenu()

while transactionType != "4":
    menuChoice = readInput("Enter your choice: ")

    if menuChoice == "1":
        transactionType = "Deposit"
        accountNumber = readInput("Enter account number: ")
        amount = float(readInput("Enter amount: "))
        processDeposit(accountNumber, amount)
    elif menuChoice == "2":
        transactionType = "Withdrawal"
        accountNumber = readInput("Enter account number: ")
        amount = float(readInput("Enter amount: "))
        processWithdrawal(accountNumber, amount)
    elif menuChoice == "3":
        transactionType = "Balance Inquiry"
        accountNumber = readInput("Enter account number: ")
        processBalanceInquiry(accountNumber)
    elif menuChoice == "4":
        transactionType = "Exit"
    else:
        displayErrorMessage("Invalid choice. Please try again.")



