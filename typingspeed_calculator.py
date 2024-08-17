from time import *
import random as r

def checkError(para, user):
    error = 0
    for i in range(len(para)):
        try:
            if para[i] != user[i]:
                error += 1
        except:
            error += 1
    return error

def speed_time(start, end, userinput):
    timeTaken = end - start
    time_R = round(timeTaken, 2) #time taken value round off
    speed = (len(userinput)/ time_R) * 60
    return round(speed)

def test():
    test = ["He who asks a question is a fool for five minutes; he who does not ask a question remains a fool forever.",
            "Failure will never overtake me if my determination to succeed is strong enough.",
            "You are braver than you believe, stronger than you seem and smarter than you think."]
    test1 = r.choice(test)
    print("****Typing Speed Calculator****")
    print(f"This is the quote for you to type: '{test1}'")
    time1 = time()
    prompt = input("Start typing here: ")
    time2 = time()

    print('Your typing speed is: ', speed_time(time1, time2, prompt), 'letters per minute')
    print('Error: ', checkError(test1, prompt))

test()
while True:
    choice = input("Do you want to try once more?(y/n): ")
    if choice.lower() == 'y':
        test()
    else:
        print("Thank you!!")
        break

