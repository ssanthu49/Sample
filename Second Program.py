B=0

while B<1:
    if B>1:break
    age=int(input('Enter your age: '))
    if age>=0 and age<=10:
        print("You Are A Child")
    elif age>20 and age<=30:
        print("YOU ARE A Bachelour")
    elif age>10 and age<=20:
        print("You Are A teenage")
    elif age>30 and age<=50:
        print("You Are A Uncle")
    elif age>50 and age<=100:
        print("You Are A Grandpa")
    else :
        B=2
        b=str(B)
        print("count"+b)
        print("You Are A GOD")
    
print("Enter to Exit")
