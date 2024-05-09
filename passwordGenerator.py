#PasswordGenerator
import string
import random
def passwordGenerator(nc,ns,nn):
    c=random.choices(string.ascii_letters, k=nc)
    s=random.choices(string.punctuation, k=ns)
    i=random.choices(string.digits, k=nn)
    f=c+s+i
    random.shuffle(f)
    password="".join(f)
    return password
print("Enter 1 If You Need Characters,Symblos,numbers")
print("Enter 2 If You Need Characters,numbers")
print("Enter 3 If You Need Characters,Symblos")
opt=-1
while True:
    try:
        o=int(input("Choose from above : "))
        if o==1 or o==2 or o==3:
            opt=o
            break
        else:
            print("Choosed Option is Out Of Availability")
            print("Please read above Displayed options")
            continue
    except ValueError:
        print("Please enter a numerical literal !!")
ps=""
if opt==1:
    while True:
        try:
            c=int(input("Enter no of characters you need in password : "))
            if c==0:
                print("You asked to have characters in password !!")
                continue
            elif c<0:
                print("Entered Negative number !!")
            else:
                break
        except ValueError:
            print("Please enter an integer !!")
    while True:
        try:
            s=int(input("Enter no of Symbols you need in password : "))
            if s==0:
                print("You asked to have symbols in password !!")
                continue
            elif s<0:
                print("Entered Negative number !!")
            else:
                break
        except ValueError:
            print("Please enter an integer !!")
    while True:
        try:
            n=int(input("Enter no of numbers you need in password : "))
            if n==0:
                print("You asked to have numbers in password !!")
                continue
            elif n<0:
                print("Entered Negative number !!")
            else:
                break
        except ValueError:
            print("Please enter an integer !!")
    ps=passwordGenerator(c,s,n)
elif opt==2:
    while True:
        try:
            c=int(input("Enter no of characters you need in password : "))
            if c==0:
                print("You asked to have characters in password !!")
                continue
            elif c<0:
                print("Entered Negative number !!")
            else:
                break
        except ValueError:
            print("Please enter an integer !!")
    while True:
        try:
            n=int(input("Enter no of numbers you need in password : "))
            if n==0:
                print("You asked to have numbers in password !!")
                continue
            elif n<0:
                print("Entered Negative number !!")
            else:
                break
        except ValueError:
            print("Please enter an integer !!")
    ps=passwordGenerator(c,0,n)
elif opt==3:
    while True:
        try:
            c=int(input("Enter no of characters you need in password : "))
            if c==0:
                print("You asked to have characters in password !!")
                continue
            elif c<0:
                print("Entered Negative number !!")
            else:
                break
        except ValueError:
            print("Please enter an integer !!")
    while True:
        try:
            s=int(input("Enter no of Symbols you need in password : "))
            if s==0:
                print("You asked to have symbols in password !!")
                continue
            elif s<0:
                print("Entered Negative number !!")
            else:
                break
        except ValueError:
            print("Please enter an integer !!")
    ps=passwordGenerator(c,s,0)
print("Password : ",ps)
#<----------------------------THANK YOU !!-------------------------------------------------------------->