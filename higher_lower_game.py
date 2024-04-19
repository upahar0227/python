from replit import clear
import random
from data import data_set
def random_account():
    return random.choice(data_set)

def Acc_desc(account):
    name=account["name"]
    description=account["description"]
    country=account["country"]
    return f"{name} a {description} from {country}"
    
def check_followers(guess,A_followers,B_followers):
    if A_followers > B_followers:
        return guess == "a"
    else:
        return guess == "b"


def game():
    score = 0
    play = True
    A=random_account()
    B=random_account()    
    while play:
        A = B
        B=random_account()
        while A == B:
            B = random_account()

        print(f"Compare A {Acc_desc(A)}")
        print("VS")
        print(f"Against {Acc_desc(B)}")
        print("\n")
        
        guess = input("who has more followers? Type A or B\n").lower()
        A_followers=A["follower_count"]
        B_followers=B["follower_count"]
        is_correct=check_followers(guess,A_followers,B_followers)

        if is_correct:
            score+=1
            print(f"you are right and your score is  {score}")
        else:
            play = False
            print(f"you are wrong and your score is  {score}")

game()
    
        
        
    

    
    
    
    
    
    
    
    
    












