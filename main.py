from preprocess import bin_alphabet

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
