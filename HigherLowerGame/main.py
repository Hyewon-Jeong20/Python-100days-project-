from art import logo, vs
from game_data import data
import random
# from replit import clear

def format_data(account) :
#Format the account data into printable format.
    return account['name'] + "," +  account['description'] + ", from" +  account['country']



def check_answer(guess, a_followers, b_followers) :
    if a_followers > b_followers :
        return  guess == "a"
    else :
        return guess == "b"


#Display art
print(logo)
score = 0
game_should_continue = True
b = random.choice(data)

#Make the game repeatable
while game_should_continue :

#Generate a random account from the game data.

#Making account at position B become the next account at position A
    a = b
    b = random.choice(data)

    while a == b :
        b = random.choice(data)

    print("Compare A:" + format_data(a))
    print(vs)
    print("Against B:" + format_data(b))


    #Ask user for a guess.
    guess = input("who has more followers? Type 'A' or 'B': ").lower()

    #Check if user is correct.
    ##Get follower count of each account.
    ##Use if statement to check if user is correct
    is_correct = check_answer(guess, a['follower_count'] , b['follower_count'] )

# Clear the screen between rounds.
#     clear()
#     print(logo)

    #Give user feedback on their guess
    #Score keeping.
    if is_correct :
        score += 1
        print(f"You're right! Current score : {score}")
    else :
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score : {score}")






















