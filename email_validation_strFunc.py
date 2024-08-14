def check():
    email = input("Enter your email address to verify: ")
    k, g, d = 0,0,0
    if len(email) >= 6:
        if email[0].isalpha():
            if ("@" in email) and (email.count('@')==1):
                if (email[-4]=='.') ^ (email[-3] == '.'):
                    for i in email:
                        if i == i.isspace():
                            k = 1
                        elif i.isalpha():
                            if i == i.upper():
                                g = 1
                        elif i.isdigit():
                            continue
                        elif i == "_" or i == "." or i == "@":
                            continue
                        else: 
                            d = 1

                    if k == 1 or g==1 or d==1:
                        print("Incorrect Email Format!!")
                    else:
                        print("Email address verified!!")
                        
                else:
                    print("Incorrect Email Format!!")
                

            else:
                print("Incorrect Email Format!!")
        else:
            print("Incorrect Email Format!!")
    else:
        print("Incorrect Email Format!!")
check()
while True:
    choice = input("Do you want to check another email address? (Y/N): ")
    if choice.lower() == "y":
        check()
    else:
        print("Thank you!, I hope that was helpful.")
        break
