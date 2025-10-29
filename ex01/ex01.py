from collections import defaultdict

def group_anagrams(strs: list[str]) -> list[list[str]]:
    groups = defaultdict(list)

    for word in strs:
        key = ''.join(sorted(word))
        # sorting the letters in the word to form a key
        groups[key].append(word)

    return list(groups.values())
    # return only the groups lists

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(group_anagrams([""]))
print(group_anagrams(["a"]))