users={
    "sahand": "1237",
    "reza" : "5647",
    "ali" : "5646"
}

enterd_username=input("please enter your username :")
enterea_password=input("please enter your password :")

if enterd_username in users and users[enterd_username]==enterea_password:
    print("loged in success")

else:
    print("the user or pass incorrect")    