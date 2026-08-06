import re

text = "My name is Sai Lahari. My phone number is 9876543210 and my email is sai@gmail.com."

pattern1 = r"My"

match_result = re.match(pattern1, text)

if match_result:
    print("Match found:", match_result.group())
else:
    print("No match found.")

pattern2 = r"\d{10}"  

search_result = re.search(pattern2, text)

if search_result:
    print("Phone Number Found:", search_result.group())
else:
    print("Phone number not found.")

email_pattern = r"\S+@\S+\.\S+"

email_result = re.search(email_pattern, text)

# cab

if email_result:
    print("Email Found:", email_result.group())
else:
    print("Email not found.")
