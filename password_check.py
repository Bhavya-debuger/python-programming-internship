import re

def check_password_strength(password):
    # Minimum length requirement
    if len(password) < 8:
        return "Weak"

    # Regex patterns
    has_number = re.search(r"\d", password)
    has_special = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)
    has_uppercase = re.search(r"[A-Z]", password)

    # Check all conditions
    if has_number and has_special and has_uppercase:
        return "Strong"
    else:
        return "Weak"

# Ask user for input
user_password = input("Enter your password: ")
strength = check_password_strength(user_password)
print(f"Password Strength: {strength}")