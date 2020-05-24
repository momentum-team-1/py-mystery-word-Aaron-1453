##open file##

import random
file = open("words.txt", "r")
text = file.read().split()
##get a random word, turn it into list - seperate letters - ##

item = random.choice(text)
word = list(item)
print(word)

##hidden is the array of underscores that the word shows up as, you append the underscore to however many letters there are in word, which was defined above and is that random word from the list##

hidden = []
for letter in word:
    hidden.append("_")

attempts = 0
max_attempts = 4

## loop till the player has won or lost##
while True:

    # display current board, guessed letters, and attempts remaining
    # just makes the underscores into a string
    hidden_string = " ".join(hidden)
    print(f"You have {attempts} attempts remaining")
    print(f'The current word is: {hidden_string}')
    break

# ask for a guess --character-- and if they guess correctly show all matched letters and print message

guess = input("Please guess a letter: ")
correct_guesses = []
wrong_guesses = []
statement = ''

for i in word:  # i in word is just letter in word but didn't want letter to mean anything but item in word
    if guess in word:
        print('first block')
        correct_guesses.append(guess)
        statement = "got em! here are your correct guesses so far"

    if guess not in word:
        print('second block')
        wrong_guesses.append(guess)
        statement = "Too bad! Give it another go!"
    break

print('correct guesses', correct_guesses)
print('wrong guesses', wrong_guesses)
print(statement)

# getting difficulty and random word##

# easy_list = [
#     word.upper()
#     for word in text
#     if 4 <= len(word) <= 6
# ]

# normal_list = [
#     word.upper()
#     for word in text
#     if 6 <= len(word) <= 8
# ]

# hard_list = [
#     word.upper()
#     for word in text
#     if 8 <= len(word)
# ]


# def get_difficulty():
#     word = ""
#     difficulty = input(
#         "Please select difficulty level, type e for easy, n for normal, and h for hard")
#     if difficulty == "e":
#         word = random.choice(easy_list)
#     elif difficulty == "n":
#         word = random.choice(normal_list)
#     elif difficulty == "h":
#         word = random.choice(hard_list)
#     return word


# if __name__ == "__main__":
#     word = (get_difficulty())
# print(f"The mystery word is {len(word)} characters long.")
# print(word)
