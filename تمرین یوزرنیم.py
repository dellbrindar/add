def passw(password):
    if len(password) <8 :
        print("your pass must be at 8 characters ")
    elif password.isnumeric():
        print("your pass must be have least one letter")
    elif password.isalpha():
        print("your pass must be have least one number")
    else :
        print("yess!")            






while True :
    password=input("please enter your pass")
    passw(password)
