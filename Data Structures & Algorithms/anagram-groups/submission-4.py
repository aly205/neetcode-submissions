class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = dict(dict())

        for word in strs:
            letters = dict()
            for s in word:
                letters[s] = letters.get(s, 0) + 1

            letters = frozenset(letters.items())

            if (letters in groups):
                groups[letters].append(word)
            else:
                groups[letters] = [word]
            
        return list(groups.values())
            
