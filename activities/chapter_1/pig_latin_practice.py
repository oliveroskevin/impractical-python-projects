print("Let's Create a Pig Latin word shall we?\n")

VOWELS =  ['a', 'e', 'i', 'o', 'u']


while True:
    word = input("Enter a word: ")
    word_list = list(word)

    if word_list[0] in VOWELS:
        word = f"{word}way"
    else:
        word_list.pop(0)
        word = f"{''.join(word_list)}ay"
    print(word)

    try_again = input("\n\nTry again? (Press Enter else n to quit)\n")

    if try_again.lower() == "n":
        break

input ("\n\nPress Enter to exit")

