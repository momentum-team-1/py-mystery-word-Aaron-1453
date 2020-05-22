import random
file = open("words.txt", "r")
text = file.read().split()
file.close()

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


def get_difficulty():
    word = ""
    difficulty = input(
        "Please select difficulty level, type e for easy, n for normal, and h for hard")
    if difficulty == "e":
        word = random.choice(easy_list)
    elif difficulty == "n":
        word = random.choice(normal_list)
    elif difficulty == "h":
        word = random.choice(hard_list)
    return word


if __name__ == "__main__":
    word = (get_difficulty())
    print(f"The mystery word is {len(word)} characters long.")
    print(word)


# def get_random_word()


# return
