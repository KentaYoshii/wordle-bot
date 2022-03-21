from preprocess import word_list
import random 
from brute import Brute


words = word_list()
goal = random.choice(words)
goal = "their"
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
                print("\n")
                _in = input(str(count) + str(dict[count]) + " attempt:")
                inputs = _in.split(" ")
                globals["word"] = inputs[0]
                globals["num"] = inputs[1]
                exec(program, globals)
                count += 1
            except Exception as e:
                print((f"Error: {e}"))
    except KeyboardInterrupt as e:
        print("\nExiting...")

        
if __name__ == "__main__":
    print("Welcome to Wordle!")
    print("Your Input should be formatted as:")
    print("<word> <number of suggestions to show>")
    print("answer:", goal)
    repl()
