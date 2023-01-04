def isCircularSentence(sentence: str) -> bool:
    words = sentence.split(" ")
    print(words)

    # print(words[0])

    for word in words:
        print(f"first letter:{word[0]} last letter: {word[-1]}")


print(isCircularSentence("leetcode exercises sound delightful"))