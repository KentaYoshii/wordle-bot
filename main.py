from preprocess import bin_alphabet

import sys



def custom_repl():
    dic = bin_alphabet()
    while True:
        print(">>")
        for line in sys.stdin:
            line = line.strip()
            if line.lower() == "exit":
                sys.exit("Exiting... Bye!")

            if line.lower() == "clear":
                print("\n" * 100)
                continue
            print(line)
            break

program = """
test(word)
"""

def test(word: str) -> None:
    print(word)

globals = {
    "test": test,
    "word": "",
}


def repl() -> None:
    try:
        while True:
            try:
                _in = input(">>> ")
                globals["word"] = _in
                exec(program, globals)
            except Exception as e:
                print((f"Error: {e}"))
    except KeyboardInterrupt as e:
        print("\nExiting...")

        
if __name__ == "__main__":
    print("Welcome to Wordle!")
    print("Your Input should be formatted as:")
    print("<word> <number of suggestions to show>")
    repl()
