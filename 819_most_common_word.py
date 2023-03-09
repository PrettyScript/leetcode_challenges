from collections import Counter

def mostCommonWord(paragraph: str, banned: list) -> str:
    
    commas_and_periods = [",", "."]
    for char in commas_and_periods:
        paragraph = paragraph.replace(char, "")
        
    words = paragraph.lower().split()
    
    common_words = Counter(words)
    print(common_words)
    common_word = max(common_words, key=common_words.get)

    for word in words:
        if word not in banned:
            return common_word

print(mostCommonWord(paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]))