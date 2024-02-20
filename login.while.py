users={
    "sahand": "1237",
    "reza" : "5647",
    "ali" : "5646"
}

enterd_username=input("please enter your username :")
enterea_password=input("please enter your password :")

while enterd_username not in users or users[enterd_username] != enterea_password :
    print(" the user or pass incorrect")
    enterd_username=input("please enter your username :")
    enterea_password=input("please enter your password :")
    
print("you logened succs")    