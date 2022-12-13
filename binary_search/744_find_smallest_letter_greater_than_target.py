def nextGreatestLetter(letters: list, target: str) -> str:

    for letter in letters:
        if letter > target:
            return letter
        elif letters[-1] <= target:
            return letters[0]


print(nextGreatestLetter(letters=["c", "f", "j"], target="a"))
print(nextGreatestLetter(letters=["c", "f", "j"], target="c"))
print(nextGreatestLetter(letters=["x", "x", "y", "y"], target="z"))
