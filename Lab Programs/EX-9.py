import re

def pos_tag(word):
    if re.fullmatch(r"(a|an|the)", word):
        return "DT (Determiner)"
    elif re.fullmatch(r".*ing", word):
        return "VBG (Verb - Gerund)"
    elif re.fullmatch(r".*ed", word):
        return "VBD (Verb - Past Tense)"
    elif re.fullmatch(r".*ly", word):
        return "RB (Adverb)"
    elif re.fullmatch(r".*ous|.*ful|.*able|.*ive", word):
        return "JJ (Adjective)"
    elif re.fullmatch(r".*s", word):
        return "NNS (Plural Noun)"
    elif re.fullmatch(r"(is|am|are|was|were)", word):
        return "VB (Verb)"
    else:
        return "NN (Noun)"

sentence = input("Enter a sentence: ").lower().split()

print("\nWord\t\tPOS Tag")
print("-" * 35)


for word in sentence:
    print(f"{word:15}{pos_tag(word)}")

#The cats are playing happily
