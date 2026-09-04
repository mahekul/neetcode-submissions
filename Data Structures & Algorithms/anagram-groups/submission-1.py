from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for i, n in enumerate(strs):
            anagrams[tuple(sorted(n))].append(n)

        return list(anagrams.values())
