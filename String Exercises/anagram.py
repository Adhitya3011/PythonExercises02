def anagram(string1, string2):
    count = 0
    for i in string1:
        for j in string2:
            if i == j:
                count += 1
                break

    if count == len(string1):
        print("The given strings are anagrams")

anagram("string", "ristgn")