from nltk.stem import PorterStemmer, WordNetLemmatizer

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

text = input("Enter a sentence: ")

words = text.split()

print("\nWord\t\tStem\t\tLemma")
print("-" * 45)

for word in words:
    stem = stemmer.stem(word)
    lemma = lemmatizer.lemmatize(word)
    print(f"{word:15}{stem:15}{lemma}")

#cat
