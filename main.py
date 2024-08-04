while True:
    n=input("enter the num")
    b=n[::-1]
    if b==n:
        print("the num is palindrome")
    else:
        print("num is not palindrome")
    repeat=input("do you want to repeat yes/no??")
    if repeat=="no" or repeat=="no":
        break