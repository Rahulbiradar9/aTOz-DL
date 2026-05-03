from collections import defaultdict

def group_anagrams(words):
    anagram_map = defaultdict(list)

    for word in words:
        key = ''.join(sorted(word))
        anagram_map[key].append(word)

    return list(anagram_map.values())


words = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = group_anagrams(words)

print(result)