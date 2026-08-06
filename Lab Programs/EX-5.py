import nltk
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()


text = input("Enter words separated by spaces: ")


words = text.split()

print("\nOriginal Word\tStemmed Word")
print("-" * 35)

for word in words:
    stem = stemmer.stem(word)
    print(f"{word:15}{stem}")
