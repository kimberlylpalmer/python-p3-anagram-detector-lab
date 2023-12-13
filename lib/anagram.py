# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()
        self.sorted_word = sorted(self.word)

    def match(self, candidates):
        matches = []
        for candidate in candidates:
            if (
                candidate.lower() != self.word
                and sorted(candidate.lower()) == self.sorted_word
            ):
                matches.append(candidate)
        return matches
