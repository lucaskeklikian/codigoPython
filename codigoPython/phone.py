import re

phone =  "12345678"

if len(phone) == 8:
   
    pattern = r"(1|8|9)[0-9]"

    match = re.match(pattern,phone)
    if match:
        print("Valid")

    else:
        print("Invalid")

else:
    print("Invalid")