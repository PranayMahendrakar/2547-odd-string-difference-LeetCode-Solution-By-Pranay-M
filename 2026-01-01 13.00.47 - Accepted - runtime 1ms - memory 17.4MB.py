class Solution:
    def oddString(self, words: List[str]) -> str:
        def get_diff(word):
            return tuple(ord(word[i+1]) - ord(word[i]) for i in range(len(word)-1))
        
        diff_to_words = {}
        for word in words:
            diff = get_diff(word)
            if diff not in diff_to_words:
                diff_to_words[diff] = []
            diff_to_words[diff].append(word)
        
        for diff, word_list in diff_to_words.items():
            if len(word_list) == 1:
                return word_list[0]
        return ""