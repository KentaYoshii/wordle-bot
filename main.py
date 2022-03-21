from preprocess import word_list
import random 
from wordle_helper import Brute


words = word_list()
goal = random.choice(words)
#goal = "their"
model  = Brute(goal)


program = """
bool, list = guess(word, goal, int(num))
if bool:
    print("Your guess is correct!")
    exit()
else:   
    print(list)
"""

globals = {
    "guess": model.guess,
    "goal": goal,
    "word": "",
    "num": 0,
}

dict = {1: "st", 2: "nd", 3: "rd", 4: "th", 5: "th"}

def repl() -> None:
    count = 1
    try:
        while True:
            try:
                if count == 6:
                    print("You have run out of guesses. The word was:", goal)
                    exit()
                print("\n")
                _in = input(str(count) + str(dict[count]) + " attempt:")
                inputs = _in.split(" ")
                globals["word"] = inputs[0]
                globals["num"] = inputs[1]
                print("\n")
                exec(program, globals)
                count += 1
            except Exception as e:
                print((f"Error: word not in the list, less than 5 letters, or already guessed."))
    except KeyboardInterrupt as e:
        print("\nExiting...")

        
if __name__ == "__main__":
    print("Welcome to Wordle!")
    print("\n")
    print("Enter a word and a number to guess the word.\n")
    print("Your Input should be formatted as:")
    print("<word> <number of suggestions to show>")
    repl()
