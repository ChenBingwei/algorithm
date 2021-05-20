# Given a non-empty list of words, return the k most frequent elements.
#
# Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency,
# then the word with the lower alphabetical order comes first.
#
# Example 1:
# Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
# Output: ["i", "love"]
# Explanation: "i" and "love" are the two most frequent words.
#     Note that "i" comes before "love" due to a lower alphabetical order.
# Example 2:
# Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
# Output: ["the", "is", "sunny", "day"]
# Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
#     with the number of occurrence being 4, 3, 2 and 1 respectively.
# Note:
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Input words contain only lowercase letters.
# Follow up:
# Try to solve it in O(n log k) time and O(n) extra space.
#
import collections
from typing import List


class Solution:
    def topKFrequent_my(self, words: List[str], k: int) -> List[str]:
        fre_dict = {}
        for i in words:
            fre_dict.setdefault(i, 0)
            fre_dict[i] += 1
        fre_dict_2 = {}
        for key, v in fre_dict.items():
            fre_dict_2.setdefault(v, [])
            fre_dict_2[v].append(key)
            fre_dict_2[v].sort()
        tmp_list = list(fre_dict_2.keys())
        tmp_list.sort(reverse=True)
        res_list = []
        for key in tmp_list:
            res_list += fre_dict_2[key]
        return res_list[:k]

    def topKFrequent_collections(self, words: List[str], k: int) -> List[str]:

        hash = collections.Counter(words)
        res = sorted(hash, key=lambda word: (-hash[word], word))
        return res[:k]


if __name__ == '__main__':
    a = Solution()
    print(a.topKFrequent_collections(["i", "love", "leetcode", "i", "love", "coding"], 2))
