import random
import os
import platform

def splitlet(query):
    return [i for i in query.lower()]

def add_(from_, to_):
    for i in range(len(from_)):
        to_.append("-")

def clear_by_machine():
    if platform.system() == "Windows":
        os.system('cls')
    elif platform.system() == "Linux":
        os.system('clear')
    else:
        os.system('clear')

def duplicates(q1, q2):
    return[k for k, j in enumerate(q1) if j == q2]

def main():
    clear_by_machine()
    game = True
    guess = 5

    with open("words.txt", "r") as f:
        list_of_words = [line.strip() for line in f]
    
    #list_of_words = ["Father", "Mother", "Apple", "Bassist"] 
    word = random.choice(list_of_words)
    word_len = len(word)
    split_word = splitlet(word)
    final_word=[]
    wrong=[]
    indexes=[]
    add_(split_word, final_word)

    print("Game started!\n\nFor commands put '?' behind your words. If you would like to guess the word, put a ':' before it. Example: ':Apple'. For every wrong letter, we remove 1 point, for every wrong guess, we remove 2 points from you.")
    input("\n\npress any key to continue...")



    while game == True:
        clear_by_machine()

        #print(split_word)
        #print(word.lower())
        print("\n\n\t\t\tWord: " + ''.join(final_word))
        print(f"\t\t\tIncorrect: {', '.join(wrong)}")
        print(f"\t\t\tRemaining guesses: {guess}\n\n")

        decision = input("> ")

        if guess > 0:
            if decision[0] == ":":
                if decision == ":"+word.lower():
                    print("You win!")
                    game=False
                else:
                    guess -=2
            elif len(decision.lower()) > 1:
                print("Only one letter, please.")
            elif decision not in split_word:
                if decision in wrong:
                    pass
                else:
                    guess -= 1
                    print(f"Wrong! You now have {guess} guesses.")
                    wrong.append(decision)
            elif decision in split_word:
                if decision in final_word:
                    print("Already said")
                else:
                    for i in duplicates(split_word, decision):
                        final_word.insert(i, decision)
                        final_word.pop(i+1)

                    if final_word == split_word:
                        print("You win!")
                        game=False
        else:
            print("Game lost")
            game=False

if __name__ == '__main__':
    main()
