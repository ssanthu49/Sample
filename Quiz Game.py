name=input('Enter Your Name : ')
print(f'Welcome {name} for the Quiz Game')
ques= [1,2,3,4,5,6,7,8,9,10]
Option=[0]*10
Answer=[4,2,1,1,3,4,3,3,2,1]
print(f'{name} Let Begin the Your Quiz')
score =0
print(f' Your Question No {ques[0]} is ')
print("In which sport do you have to use a gun?")
print( "1. Hankumdo 2. Darts 3. Javelin fish 4. Biatlon")
Option[0]=int(input("Your Option : "))
print("What means a blue flag at the racecircuit?")
print( "1. The race is stopped 2. You have to let a faster car pass 3. There is danger on the track 4. There is a very slow car on the track")
Option[1]=int(input("Your Option : "))
print("What is the weight of a discus?")
print( "1. Men 2kg, women 1kg 2. For men and women 2kg 3. Men 2.5kg, women 2kg 4. For men and women 2.5kg")
Option[2]=int(input("Your Option : "))
print("What is not a kind of horse sport?")
print( "1. Vasning 2. Dressage 3. Polo 4. Voltige")
Option[3]=int(input("Your Option : "))
print("How manny balls are there on a snooker table?")
print( "1. 19 2. 18 3. 22 4. 21")
Option[4]=int(input("Your Option : "))
print("What ball has the largest diameter?")
print( "1.  squash ball 2. a golf ball 3. TennisBall 4. a table tennis ball")
Option[5]=int(input("Your Option : "))
print("What is the maximum number of points that can be scored in a bowling game (a perfect game)?")
print( "1. 270 2. 330 3. 300 4. 360")
Option[6]=int(input("Your Option : "))
print("Which sport isn't played on ice?")
print( "1. Shorttrack 2. Bobsledding 3. Lacrosse 4. Ice hockey")
Option[7]=int(input("Your Option : "))
print("What is the distance between the hurdles at 400m hurdles for men?")
print( "1. 15 meters 2. 35 meters 3. 25 meters 4. 55 meters")
Option[8]=int(input("Your Option : "))
print("What is not allowed in speed walking")
print( "1. Have your 2 legs at the same time of the ground 2. Walking slower then 10km/h 3. To old your legs 4. Make a step that is smaller then 1 meter")
Option[9]=int(input("Your Option : "))

for i,j in zip(Answer, Option):
    if i==j:
        score+=1
print(f' Congragulation {name} you scored perfect 10') if score== 10 else print(f' {name} Your scored {score} out of 10')
input("Press Enter to EXIT")
