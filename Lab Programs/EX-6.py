# Basic Bigram Model for Text Generation

import random

# Input text
text = input("Enter a sentence: ")

# Tokenize the text into words
words = text.split()

# Create bigrams
bigrams = {}

for i in range(len(words) - 1):
    word = words[i]
    next_word = words[i + 1]

    if word not in bigrams:
        bigrams[word] = []

    bigrams[word].append(next_word)

print("\nBigram Dictionary:")
for key, value in bigrams.items():
    print(key, "->", value)


start_word = random.choice(words)
generated_text = [start_word]

for _ in range(9):  
    if start_word in bigrams:
        next_word = random.choice(bigrams[start_word])
        generated_text.append(next_word)
        start_word = next_word
    else:
        break

print("\nGenerated Text:")
print(" ".join(generated_text))

#the cat sat on the mat the cat ate the fish
