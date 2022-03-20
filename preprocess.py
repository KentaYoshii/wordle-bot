
alpha_to_bin = {"a": [], "b": [], "c": [], "d": [], "e": [], "f": [], "g": [], "h": [], "i": [], "j": [], "k": [], "l": [], "m": [], "n": [], "o": [], "p": [], "q": [], "r": [], "s": [], "t": [], "u": [], "v": [], "w": [], "x": [], "y": [], "z": []}

def bin_alphabet():
    with open("data/word.txt") as f:
        for line in f:
            line = line.strip()
            for char in line:
                alpha_to_bin[char].append(line)
    return alpha_to_bin

def word_list():
    with open("data/word.txt") as f:
        return [line.strip() for line in f]
        