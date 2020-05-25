##open file##

import random


def get_difficulty():
    word = ""
    difficulty = input(
        "Please select difficulty level, type e for easy, n for normal, and h for hard ")
    if difficulty == "e":
        word = random.choice(easy_list)
    elif difficulty == "n":
        word = random.choice(normal_list)
    elif difficulty == "h":
        word = random.choice(hard_list)
    return word


# if __name__ == "__main__":

file = open("words.txt", "r")
text = file.read().split()
##get a random word, turn it into list - seperate letters - ##

# item = random.choice(text)
# word = list(item)
# print(word)

##hidden is the array of underscores that the word shows up as, you append the underscore to however many letters there are in word, which was defined above and is that random word from the list##


attempts = 0
max_attempts = 4


easy_list = [
    word.upper()
    for word in text
    if 4 <= len(word) <= 6
]

normal_list = [
    word.upper()
    for word in text
    if 6 <= len(word) <= 8
]

hard_list = [
    word.upper()
    for word in text
    if 8 <= len(word)
]


word = (get_difficulty())
# make word capitalized
word = list(word.upper())


hidden = []
for letter in word:
    hidden.append("_")


print(f"The mystery word is {len(word)} characters long.")
print("".join(word))

## loop till the player has won or lost##
is_game_over = False
while not is_game_over:

    # display current board, guessed letters, and attempts remaining
    # just makes the underscores into a string
    hidden_string = " ".join(hidden)
    print(f"You have {max_attempts - attempts} attempts remaining")
    # print(f'The current word is: {hidden_string}')
    # ask for a guess --character-- and if they guess correctly show all matched letters and print message

    guess = input("Please guess a letter: ")
    correct_guesses = []
    wrong_guesses = []
    statement = ''

    # make the guess capitalized
    guess = guess.upper()

    if guess in word:
        # Iterate over string with index using range(), string being the letters of the word
        for i in range(len(word)):
            # range(len (stringObj) ) function will generate the sequence from 0 to n -1 ( n is size of string) . Now iterate over this sequence and for each index access the character from string using operator
            character = word[i]  # use those [] to catch each index
            if character == guess:
                hidden[i] = word[i]
                word[i] = "_"
        print(f'nice guess! "{guess}" is in the word')
        print("".join(hidden))
        # print("".join(word))
    elif guess not in word:
        print(f'Whoops! It looks like "{guess}" is not in this word')
        attempts += 1
        # print(word)
    # getting difficulty and random word##
    # running out of underscores has to end the game
    if (all('_' == char for char in word)):  # i don't see why != isn't used here
        print("You've done it!")
        is_game_over = True
    # running out of guesses has to end the game

    if attempts >= max_attempts:
        print("sorry you are out of guesses and therefore out of time")
        is_game_over = True
