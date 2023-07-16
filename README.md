Problem statement : develop aprogram to simplify tranasactions for bank tellers by providing an easier interface
Sub- problems: user authentication , transaction processing and user interface
Sub- Solution : User authentication , Customer information management , Transaction approval workflow
Define variables :
Username: string (to store the entered username)
Password: string(to store the entered password)
Authenticated : Boolean ( to rack the authentication status)
B) control strucutures:
Conditional : if –else statement. Using the if statement it shall detect if the user name and password is valid and invalid
Transaction Processing 
Define Variables:
TransactionType: string(to store the type of transaction, .g deposit, withdrawal, balance inquiry)
accountNumber: string(to store the account number of the customer)
amount: float (to store the transaction amount)
B) control structures :
Conditional : switch-case statement 
Lterative: while loop
Conditional: if-else statement
User Interface
Define Variables :
menuChoice: string( to store the users menu choice)
B) Control Structures:
Lterative: do-while loop
Conditional : if-else statement



FUNCTIONS GOING TO BE USED
# User Authentication
def validateCredentials(username, password):
    # Val.idate username and password against database or authentication system
    # Return True if valid, False otherwise
    # Implement your own validation logic here
    valid_username = "admin"
    valid_password = "password123"
    return username = valid_username and password = valid_password

# Transaction Processing
def processDeposit(accountNumber, amount):
    # Process the deposit transaction
    # Perform necessary validation and database operations
    # Implement your own deposit logic here
    print(f"Processing deposit of {amount} into account {accountNumber}")

def processWithdrawal(accountNumber, amount):
    # Process the withdrawal transaction
    # Perform necessary validation and database operations
    # Implement your own withdrawal logic here
    print(f"Processing withdrawal of {amount} from account {accountNumber}")

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
    print("Main Menu ")
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






