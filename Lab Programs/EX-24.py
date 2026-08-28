def recognize_dialog_act(sentence):
    text = sentence.lower()

    if "?" in text or text.startswith(("what", "why", "when", "where", "who", "how", "can", "do", "is")):
        return "Question"
    elif text.startswith(("please", "could you", "would you", "tell me")):
        return "Request"
    elif any(word in text for word in ["thank", "thanks"]):
        return "Thanking"
    elif any(word in text for word in ["hello", "hi", "hey"]):
        return "Greeting"
    elif any(word in text for word in ["bye", "goodbye", "see you"]):
        return "Goodbye"
    elif any(word in text for word in ["yes", "sure", "okay", "agree"]):
        return "Agreement"
    else:
        return "Statement"

dialog = input("Enter a dialog: ")

for sentence in dialog.split("."):
    sentence = sentence.strip()
    if sentence:
        print(sentence, "->", recognize_dialog_act(sentence))

"""
Hello. Can you help me with my project? Please explain Python. Thank you. Goodbye.
"""
