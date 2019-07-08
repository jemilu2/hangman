

class HangmanLexicon:

    def __init__(self):
        with open("HangmanLexicon.txt") as f:
            self._words = f.readlines()
        
    def size(self):
        return len(self._words)

    def get_word(self,index):
        if index < self.size():
            return self._words[index]
        else:
            return None