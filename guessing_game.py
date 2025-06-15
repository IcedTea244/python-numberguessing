import random
def guess(user,number):
    if(user>number):
        print("Too High 😥")
    elif(user<number):
        print("Too low 😥")
    elif(user==number):
        print("Yah,you hav won. 😊")
        return  True
    return False

        
while True:
    try:
        level=input("Easy \t Medium\t Hard-> ").lower()
        count=0
        won=False
        if (level=="easy"):      
            number=random.randint(1,10)
            while(count<3):
                user=int(input("Enter the number:"))
                if(user<1 or user>10):
                    print("Try between 1 and 10")
                count+=1
                print(f"Attempts left:{3-count}")
                if guess(user,number):
                    won=True
                    break
            
        elif(level=="medium"):
            number=random.randint(1,50)
            while(count<5):
                user=int(input("Enter the number:"))
                if(user<1 or user>50):
                    print("Try between 1 and 50")
                count+=1
                print(f"Attempts left:{5-count}")
                if guess(user,number):
                    won=True
                    break

        elif(level=="hard"):
            number=random.randint(1,100)
            while(count<10):
                user=int(input("Enter the number:"))
                if(user<1 or user>100):
                    print("Try between 1 and 100")
                count+=1
                print(f"Attempts left:{10-count}")
                if guess(user,number):
                    won=True
                    break

        else:
            print("Enter valid level ")
            continue
    
        if not won:
            print(f"sorry,you have lost 🥲. The answer is {number}")

    except Exception as e:
        print("ERROR...Enter a valid input ")

    finally:
        restart=input("Do you want to play again or no?yes/no\t").lower()
        if (restart!="yes"):
            print("Bye for time being")
            break
  

