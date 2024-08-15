import re
email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$" 
# '\' is used to search character in regex, '?' the serach item is either 0 or only 1, \w search the special symbol from behind
user_email = input("Enter your email: ")
def check():
    if re.search(email_condition, user_email):
        print("Correct email format. Verified!!!")
    else:
        print("Incorrect email format.")
check()
while True:
    choice = input("Do you wanna try next email? (Y/N):")
    if choice.lower() == 'y':
        check()
    else:
        print("Thank you!")
        break



