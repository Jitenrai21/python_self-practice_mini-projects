import phonenumbers
from phonenumbers import timezone, geocoder, carrier
def displayDetails():
    number = input("Enter your phone number(with country code): ")
    phone = phonenumbers.parse(number)
    time = timezone.time_zones_for_number(phone)
    car = carrier.name_for_number(phone,'en')
    reg = geocoder.description_for_number(phone, 'en')
    print(phone)
    print(time)
    print(car)
    print(reg)
displayDetails()
while True:
    choice = input("Do you want to check for another number(y/n): ")
    if choice.lower == 'y':
        displayDetails()
    else:
        print("Thank you!")
        break