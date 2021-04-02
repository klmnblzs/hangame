
try:
    from colorama import init, Fore, Back, Style
    import random
    import os
    import sys
    import platform

    init(autoreset=True)
except:
    print(f"Install required libraries! (COLORAMA)")

class Hangman:
    def __init__(self):
        self.guesses = 5

    def splitlet(self, query):
        return [i for i in query.lower()]

    def add_(self, from_, to_):
        for i in range(len(from_)):
            to_.append("-")

    def clear_by_machine(self):
        if platform.system() == "Windows":
            os.system('cls')
        elif platform.system() == "Linux":
            os.system('clear')
        else:
            os.system('clear')

    def duplicates(self, q1, q2):
        return[k for k, j in enumerate(q1) if j == q2]

    def tutorial(self):
        h = Hangman()
        h.clear_by_machine()
        print(Fore.YELLOW + "- GAME STARTED\n\n")
        print(Fore.YELLOW + "> Guessing:\n - :word\n - Example: :unusual\n - If you win you will see this message: " + Fore.GREEN + "Congratulations! You win!\n\n")
        print(Fore.YELLOW + "> Points:\n - You have 5 guesses by default.\n - If you get a letter wrong the game substracts " + Fore.RED + " ONE " + Fore.YELLOW + " point.\n - If you get a guess wrong the game substracts " + Fore.RED + " TWO " + Fore.YELLOW + " points.\n - If you lose you will see this message: "+ Fore.RED + "You lose! The word was: {word}\n\n")

        input(Fore.YELLOW + "Press any key to continue...")
        h.main()

    def confirmation(self):
        h = Hangman()
        decision = input("Continue? (Y/n): ")

        if decision.lower() in ["y", ""]:
            h.tutorial()
        elif decision.lower() == "n":
            sys.exit()

    def main(self):
        h = Hangman()
        h.clear_by_machine()
        game = True
        guess = h.guesses

        with open("words.txt", "r") as f:
            list_of_words = [line.strip() for line in f]

        word = random.choice(list_of_words)
        word_len = len(word)
        split_word = h.splitlet(word)
        final_word=[]
        wrong=[]
        indexes=[]
        h.add_(split_word, final_word)

        while game == True:
            h.clear_by_machine()

            texts = [f"\n\n\t\tWord: {''.join(final_word)}", f"\t\tIncorrect: {', '.join(wrong)}", f"\t\tRemaining guesses: {guess}\n\n"]

            for i in texts:
                print(Fore.YELLOW + i)

            decision = input(Fore.YELLOW + "\t\t> ")

            if guess > 1:
                if decision[0] == ":":
                    if decision.lower() == ":"+word.lower():
                        h.clear_by_machine()
                        print(Fore.GREEN + "Congratulations! You win!")
                        game=False
                        h.confirmation()
                    else:
                        guess -= 2
                elif len(decision.lower()) > 1:
                    pass
                elif decision.lower() not in split_word:
                    if decision.lower() in wrong:
                        pass
                    else:
                        guess -= 1
                        wrong.append(decision.lower())
                elif decision.lower() in split_word:
                    if decision.lower() in final_word:
                        pass
                    else:
                        for i in h.duplicates(split_word, decision.lower()):
                            final_word.insert(i, decision.lower())
                            final_word.pop(i+1)
                            texts.append("ok")

                        if final_word == split_word:
                            h.clear_by_machine()
                            print(Fore.GREEN + "Congratulations! You win!")
                            game=False
                            h.confirmation()
            else:
                h.clear_by_machine()
                print(Fore.RED + f"You lose! The word was: {word}")
                game=False
                h.confirmation()

if __name__ == '__main__':
    h = Hangman()
    h.tutorial()
