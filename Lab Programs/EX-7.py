import nltk

text = input("Enter a sentence: ")

words = nltk.word_tokenize(text)
pos_tags = nltk.pos_tag(words)

print("\nWord\t\tPart of Speech")
print("-" * 35)

for word, tag in pos_tags:
    print(f"{word:15}{tag}")

#The cat is sleeping on the mat.
