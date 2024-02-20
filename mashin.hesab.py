# دریافت دو عدد از کاربر
num1 = float(input("عدد اول را وارد کنید: "))
num2 = float(input("عدد دوم را وارد کنید: "))

# انتخاب یک عملیات ریاضی
operation = input("عملیات مورد نظر را انتخاب کنید (+, -, *, /): ")

# اعمال عملیات و چاپ نتیجه
if operation == '+':
    print(num1 + num2)
elif operation == '-':
    print(num1 - num2)
elif operation == '*':
    print(num1 * num2)
elif operation == '/':
    if num2 != 0:
        print(num1 / num2)
    else:
        print("تقسیم بر صفر ممنوع!")
else:
    print("عملیات نامعتبر")
