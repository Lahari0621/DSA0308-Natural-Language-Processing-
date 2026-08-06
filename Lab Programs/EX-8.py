pos_prob = {
    "the": {"DT": 1.0},
    "a": {"DT": 1.0},
    "cat": {"NN": 0.9, "VB": 0.1},
    "dog": {"NN": 1.0},
    "runs": {"VBZ": 0.8, "NNS": 0.2},
    "run": {"VB": 0.7, "NN": 0.3},
    "is": {"VBZ": 1.0},
    "sleeping": {"VBG": 1.0},
    "on": {"IN": 1.0},
    "mat": {"NN": 1.0},
    "quickly": {"RB": 1.0}
}

sentence = input("Enter a sentence: ").lower().split()

print("\nWord\t\tPredicted POS")
print("-" * 35)

for word in sentence:
    if word in pos_prob:
        tag = max(pos_prob[word], key=pos_prob[word].get)
    else:
        tag = "UNK"  

    print(f"{word:15}{tag}")
#The cat is sleeping on the mat
