from preprocess import bin_alphabet, word_list

dict = bin_alphabet()

class Brute:

    def __init__(self, goal):
        self.goal = goal
        self.posWordList = word_list()
        self.word = None
        self.curMatchingPos = {0: None, 1: None, 2: None, 3: None, 4: None}
        self.curContains = {}
        self.corPosScore = 1
        self.corConScore = 0.5
        self.notContains = set()
    
    def drop_words(self):
        resList = [] # this list will contain the words that have letters that are not in the notContains set
        for word in self.posWordList:
            count = 0
            for char in word:
                if char in self.notContains:
                    count += 1
            if count != len(word):
                resList.append(word)

        self.posWordList = resList
                    
            

    def guess(self, word, goal, numToReturn):
        self.word = word
        self.posWordList.remove(word)
        if self.word == goal:
            return True, []
        self.trimSet(self.word, goal)
        self.drop_words()

        word_to_val = self.scoreWords(self.word)
        sorted_word_to_val = sorted(word_to_val.items(), key=lambda x: x[1], reverse=True)
        print(self.curMatchingPos, "matching set")
        print(self.curContains, "contains set")
        return False, sorted_word_to_val[:numToReturn]

    def trimSet(self, word, goal):
        self.retMatchingPos(word, goal) # returns dic with idx -> char mapping
        self.retContains(word, goal)
        curNotContains = [char for char in word if char not in self.curContains]
        curNotContains = [char for char in curNotContains if char not in self.curMatchingPos.values()]
        self.notContains.update(curNotContains)
        
    def scoreWords(self, word):
        word_to_val = {}
        for word in self.posWordList:
            point = 0
            for i in range(len(word)):
                if word[i] == self.curMatchingPos[i]:
                    point += self.corPosScore
                elif word[i] in self.curContains:
                    if i in self.curContains[word[i]]:
                        point += self.corConScore
            word_to_val[word] = point
        return word_to_val
            
    def howManyContains(self, word, goal):
        count = 0
        for i in range(len(word)):
            if word[i] in goal and word[i] != goal[i]:
                count += 1
        return count

    def howManyMatch(self, word, goal):
        count = 0
        for i in range(len(word)):
            if word[i] == goal[i]:
                count += 1
        return count

    def retMatchingPos(self, word, goal):
        for i in range(len(word)):
            if word[i] == goal[i]:  # if the char at the same index is the same
                self.curMatchingPos[i] = word[i] # add it to the machingPos set

    def retContains(self, word, goal):
        for i in range(len(word)):
            if word[i] in goal and word[i] != goal[i]:
                if word[i] not in self.curContains:
                    self.curContains[word[i]] = []
                    self.curContains[word[i]].append(i)
                elif i not in self.curContains[word[i]]:
                    self.curContains[word[i]].append(i)