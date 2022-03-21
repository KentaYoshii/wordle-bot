from preprocess import word_list
import random 
from brute import Brute


words = word_list()
goal = random.choice(words)
model  = Brute(goal)


program = """
bool, list = guess(word, goal, int(num))
if bool:
    print("Your guess is correct!")
    exit()
else:   
    for word in list:
        print(word)
"""

globals = {
    "guess": model.guess,
    "goal": goal,
    "word": "",
    "num": 0,
}

def repl() -> None:
    try:
        while True:
            try:
                _in = input(">>> ")
                inputs = _in.split(" ")
                globals["word"] = inputs[0]
                globals["num"] = inputs[1]
                exec(program, globals)
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
