

class HangmanLexicon:

    def __init__(self):
        self._words = [
            "BUOY","COMPUTER","CONNOISSEUR",
            "DEHYDRATE","FUZZY","HUBBUB",
            "KEYHOLE","QUAGMIRE","SLITHER",
            "ZIRCON"
        ]
    
    def size(self):
        return len(self._words)

    def get_word(self,index):
        if index < self.size():
            return self._words[index]
        else:
            return None