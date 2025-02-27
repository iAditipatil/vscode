try:
    a=int(input("enter num1="))
    b=int(input("enter num2="))
    c=a/b
except ZeroDivisionError:
    print("number is devided by zero")
else:
    print("c=",c)
finally:
    print("end of program")