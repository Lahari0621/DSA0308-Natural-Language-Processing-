Word=input("enter string")
sentence = Word.split()

tags = {
    "I": "PRP",
    "can": "NN",
    "fish": "NN"
}

print("Initial Tags:")
for word in sentence:
    print(f"{word} --> {tags[word]}")

def apply_rules(words, tags):
    for i in range(1, len(words)):
        if words[i] == "can" and tags[words[i]] == "NN":
            if tags[words[i-1]] == "PRP":
                tags[words[i]] = "MD"

    return tags

updated_tags = apply_rules(sentence, tags)

print("\nTags After Applying Transformation Rule:")
for word in sentence:
    print(f"{word} --> {updated_tags[word]}")
