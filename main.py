# Create a game that does the following:
from itertools import filterfalse

# 1. Shows the name, handle, and bio of two randomly selected influencers from the dataset. DONEZO

# 2. Takes user input to guess which of the two influencers has more followers. DONEZO

# 3. Evaluates which influencer has more followers and compares the correct answer to the user's guess.

# 4. Upon a correct guess, brings up a new random influencer to compare to the "winner" of the prior round.

# 5. Upon an incorrect guess, selects two entirely new influencers at random from the remaining options.

# 6. Keeps track of how many times the user guesses incorrectly.

# 7. Ends the game after 5 incorrect guesses.

# 8. Ensures no "losing" influencer is offered to the user more than once.

from data import influencers
import random

print("Social Media Game")
print("You currently have 5 lives")
print("")


def chosen_two_randos(exclude):  #picks out a random influencer from list
    candidates = [influencer for influencer in influencers if influencer not in exclude]
    return random.sample(candidates, 2)

def chosen_one_rando(exclude=[]):  #picks out another random influencer from list
    candidates = [influencer for influencer in influencers if influencer not in exclude]
    return random.sample(candidates, 1)

def print_influencer(result1):
    name = result1['name']
    print(name)
    handle = result1['handle']
    print(handle)
    bio = result1['brief_bio']
    print(bio)
    following = result1['followers']


def main():   #main game function, contains one whole round
    lives = 3
    used_influencers = []   #defines list of used influencers
    chosen_winner = False

    while lives > 0:

        if not chosen_winner:
            influencer_1, influencer_2 = chosen_two_randos(used_influencers)
        else:
            print(f"THIS IS RUNNING: {influencer_1["name"]}")
            influencer_2 = chosen_one_rando(used_influencers)[0]
            chosen_winner = False

        print_influencer(influencer_1)
        print_influencer(influencer_2)

        while True:
            # global influencer_1, influencer_2, chosen_winner
            try:
                question = int(input("Who has more followers? (1/2): "))
                if question in [1, 2]:  #for valid answers...
                    break
                else:
                    print("Please enter 1 or 2.")
            except ValueError:          #for invalid answers...
                print("Invalid input. Please enter 1 or 2.")

        # Determine influencer with highest following
        if (question == 1 and influencer_1['followers'] > influencer_2['followers']) or \
                (question == 2 and influencer_2['followers'] > influencer_1['followers']):
            print("Correct")
            print("")
            used_influencers.append(influencer_1 if question == 1 else influencer_2)
            if question == 2 and influencer_2['followers'] > influencer_1['followers']:
                print("Correct")
                influencer_1 = influencer_2
            chosen_winner = True
        else:
            print("Incorrect")
            print("")
            lives -= 1
            print(f"You have {lives} lives remaining.")
            used_influencers.extend([influencer_1, influencer_2])  # Mark both influencers as used
        print("")
        if lives == 0:    #play again function
            print("Game over, you lose.")
            play_again = input("Would you like to play again? (yes/no):").lower()
            if play_again == "yes":
                main()   #runs main function again
            else:
                print("Thank you for playing!")
                break   #cancels function and ends game


if __name__ == "__main__":
    main()

# from data import influencers
#
# import random
#
# print("Social Media Game")
# print("You currently have 3 lives")
# print("")
#
# # variables
# influencers = influencers
# name = influencers[0]
# handle = influencers[0]
# brief_bio = influencers[0]
#
# influencer_1 = influencers[0]
# influencer_2 = influencers[1]
#
#
# namez = influencers[1]
# handlez = influencers[1]
# brief_bioz = influencers[1]
#
# def chosen_rando():
#     random_index = random.randint(0, len(influencers) - 1)
#     result1 = influencers[random_index]
#     return result1
#
# def print_influencer(result1):
#     name = result1['name']
#     print(name)
#     handle = result1['handle']
#     print(handle)
#     bio = result1['brief_bio']
#     print(bio)
#     following = result1['followers']
#     return result1
#
# def main():
#     global influencers
#     global influencer_1
#     global influencer_2
#     current_winner = None
#     lives = 3
#     while lives > 0:
#
#         print_influencer(influencer_1)
#         print_influencer(influencer_2)
#
#         question = int(input("Who has more followers? (1/2)"))
#
#         influencers.remove(influencer_1)
#         influencers.remove(influencer_2)
#
#             # Selection of influencer when input is typed
#         if question == 1:
#             chosen_influencer = influencer_1
#             compared_influencer = influencer_2
#         else:
#             chosen_influencer = influencer_2
#             compared_influencer = influencer_1
#
#         if chosen_influencer['followers'] > compared_influencer['followers'] and question == 1:
#             print("Correct")
#             # chosen_influencer = influencer_2
#         elif chosen_influencer['followers'] > compared_influencer['followers'] and question != 1:
#             print("Correct")
#             influencer_1 = chosen_influencer
#         else:
#             print("Incorrect")
#             current_winner = None  # Reset winner if incorrect
#             lives -= 1
#             # compared_influencer = influencer_1
#             print("You have" + str(lives) + "lives remaining.")
#             print("")
#
#         if lives == 0:
#             print("Game over, you lose.")
#             play_again = input("Would you like to play again?")
#             if play_again == "yes" or "Yes":
#                 main()
#             else:
#                 print("Thank you for playing!")
# main()




