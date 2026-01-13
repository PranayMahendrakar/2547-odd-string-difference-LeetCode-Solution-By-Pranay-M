class Solution:
    def oddString(self, words: List[str]) -> str:
        def get_diff(word):
            return tuple(ord(word[i+1]) - ord(word[i]) for i in range(len(word)-1))
        
        diffs = [get_diff(w) for w in words]
        if diffs[0] != diffs[1]:
            return words[0] if diffs[1] == diffs[2] else words[1]
        for i in range(2, len(words)):
            if diffs[i] != diffs[0]:
                return words[i]
        return ""