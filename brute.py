from preprocess import bin_alphabet, word_list

dict = bin_alphabet()

class Brute:

    def __init__(self, goal):
        self.goal = goal
        self.posWordList = word_list()
        self.curMatchingPos = set()
        self.curContains = set()
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
        print(self.curMatchingPos, "matching set")
        print(self.curContains, "contains set")
        if word == goal:
            return True, []
        self.trimSet(word, goal)
        self.drop_words()
        word_to_val = self.scoreWords(word)
        sorted_word_to_val = sorted(word_to_val.items(), key=lambda x: x[1], reverse=True)
        return False, sorted_word_to_val[:numToReturn]

    def trimSet(self, word, goal):
        matchingPos = self.retMatchingPos(word, goal)
        charContained = self.retContains(word, goal)
        charContained = [char for char in charContained if char not in matchingPos]
        self.curContains.update(charContained)
        self.curMatchingPos.update(self.curMatchingPos)
        curNotContains = [char for char in goal if char not in self.curContains]
        curNotContains = [char for char in curNotContains if char not in self.curMatchingPos]
        self.notContains.update(curNotContains)
        
    def scoreWords(self, word):
        word_to_val = {}
        for word in self.posWordList:
            total_score = self.corPosScore * self.howManyMatch(word, self.goal) + self.corConScore * self.howManyContains(word, self.goal)
            word_to_val[word] = total_score
        return word_to_val
            
    def howManyContains(self, word, goal):
        contains = self.retContains(word, goal)
        return len(contains)

    def howManyMatch(self, word, goal):
        matchingPos = self.retMatchingPos(word, goal)
        return len(matchingPos)

    def retMatchingPos(self, word, goal):
        matchingPos = []
        for i in range(len(word)):
            if word[i] == goal[i]:
                matchingPos.append(i)
        return matchingPos

    def retContains(self, word, goal):
        contains = []
        for i in range(len(word)):
            if word[i] in goal:
                occurrence = goal.count(word[i])
                for i in range(occurrence):
                    contains.append(word[i])
        return contains