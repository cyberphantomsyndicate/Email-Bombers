import smtplib
import hashlib
import time
from colorama import Fore, init
import pyfiglet
import sys

init(autoreset=True)

def generate_hacker_logo():
    hacker_logo = pyfiglet.figlet_format("CPS", font="slant")
    return hacker_logo

def type_writer_effect(message, speed=0.1):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

quote1 = "If you've been betrayed in love, make sure to tell me, all characterless are our enemies"
quote2 = "We don't hack to impress, we hack to express."

print(Fore.GREEN + generate_hacker_logo())
print("\n")
print("\n--- Incoming Message ---\n")
time.sleep(1)
type_writer_effect(">>> " + quote1, speed=0.05)
type_writer_effect(">>> " + quote2, speed=0.05)

MAX_ATTEMPTS = 3
LOCK_DURATION = 30

try:
    with open("pass.txt", "r") as f:
        HASHED_PASSWORD = f.read().strip()
except FileNotFoundError:
    print(Fore.RED + "Password file 'pass.txt' not found.")
    exit(1)

def check_password():
    attempts = 0
    while attempts < MAX_ATTEMPTS:
        entered_password = input(Fore.YELLOW + "Enter Code To Unlock The Tool: ")
        hashed_entered_password = hashlib.sha256(entered_password.encode()).hexdigest()
        
        if hashed_entered_password == HASHED_PASSWORD:
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

if not check_password():
    exit("Exiting program due to failed unlock attempts.")

def send_email(to_email, from_email, password, subject, message, server="smtp.gmail.com", port=587):
    try:
        with smtplib.SMTP(server, port) as smtp:
            smtp.starttls()
            smtp.login(from_email, password)
            email_message = f"Subject: {subject}\n\n{message}"
            smtp.sendmail(from_email, to_email, email_message)
            print(Fore.GREEN + f"Email sent to {to_email}")
    except Exception as e:
        print(Fore.RED + f"Failed to send email: {e}")

def main():
    print(Fore.YELLOW + "=== Educational Email Sender ===")
    from_email = input("Enter your email address: ")
    password = input("Enter your email password: ")
    to_email = input("Enter the recipient's email address: ")
    subject = input("Enter the subject of the email: ")
    message = input("Enter the message content: ")
    count = int(input("Enter the number of emails to send (educational limit): "))

    for i in range(count):
        print(Fore.BLUE + f"Sending email {i + 1} of {count}...")
        send_email(to_email, from_email, password, subject, message)
        time.sleep(1)

if __name__ == "__main__":
    main()
