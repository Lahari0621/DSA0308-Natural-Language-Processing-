import re


def contains_vowel(word):
    vowels = "aeiou"
    for ch in word:
        if ch in vowels:
            return True
    return False


def measure(word):
    vowels = "aeiou"
    m = 0
    prev_vowel = False

    for ch in word:
        is_vowel = ch in vowels
        if prev_vowel and not is_vowel:
            m += 1
        prev_vowel = is_vowel

    return m


def ends_double_consonant(word):
    if len(word) < 2:
        return False
    return (
        word[-1] == word[-2]
        and word[-1] not in "aeiou"
    )


def cvc(word):
    if len(word) < 3:
        return False

    c1, v, c2 = word[-3], word[-2], word[-1]

    return (
        c1 not in "aeiou"
        and v in "aeiou"
        and c2 not in "aeiou"
        and c2 not in "wxy"
    )




def step1b(word):

   
    if word.endswith("eed"):
        stem = word[:-3]
        if measure(stem) > 0:
            return stem + "ee"

    changed = False


    if word.endswith("ed"):
        stem = word[:-2]
        if contains_vowel(stem):
            word = stem
            changed = True

    elif word.endswith("ing"):
        stem = word[:-3]
        if contains_vowel(stem):
            word = stem
            changed = True

    
    if changed:

        if word.endswith("at"):
            word += "e"

        elif word.endswith("bl"):
            word += "e"

        elif word.endswith("iz"):
            word += "e"

        elif ends_double_consonant(word) and word[-1] not in "lsz":
            word = word[:-1]

        elif measure(word) == 1 and cvc(word):
            word += "e"

    return word



words = [
    "agreed",
    "plastered",
    "bled",
    "motoring",
    "sing",
    "hopping",
    "filing",
    "conflated",
    "troubled",
    "sized"
]

for w in words:
    print(f"{w:12} -> {step1b(w)}")
