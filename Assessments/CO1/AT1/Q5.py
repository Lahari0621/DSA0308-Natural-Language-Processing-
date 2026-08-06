import re

email_pattern = re.compile(
    r'^[A-Za-z0-9][A-Za-z0-9._%+-]*@[A-Za-z0-9.-]+\.(com|org|edu|in)$'
)


emails = [
    "john.doe123@gmail.com",
    "student01@college.edu",
    "info_company@company.in",
    "user.name@domain.org",
    "invalid@email",
    "@gmail.com",
    "user@.com"
]
print("Email Validation Results:")
for email in emails:
    if email_pattern.fullmatch(email):
        print(email, "-> Valid Email ID")
    else:
        print(email, "-> Invalid Email ID")
