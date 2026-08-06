def generate_plural(noun):

    if noun.endswith(("s", "x", "z", "ch", "sh")):
        return noun + "es"

    
    elif noun.endswith("y") and len(noun) > 1 and noun[-2] not in "aeiou":
        return noun[:-1] + "ies"

   
    elif noun.endswith("f"):
        return noun[:-1] + "ves"
    elif noun.endswith("fe"):
        return noun[:-2] + "ves"

    else:
        return noun + "s"


noun = input("Enter a singular noun: ")
plural = generate_plural(noun)

print("Singular Noun :", noun)
print("Plural Noun   :", plural)
