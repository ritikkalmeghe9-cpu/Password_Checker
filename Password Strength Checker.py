import re

def check_password_strength(password):
    # Score initialization
    score = 0

    # Check length
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1

    # Check for uppercase, lowercase, numbers, and special chars
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[@$!%*?&#]", password):
        score += 1

    # Common weak passwords list
    weak_passwords = ["123456", "password", "qwerty", "abc123", "admin"]
    if password.lower() in weak_passwords:
        return "❌ Very Weak: Commonly used password!"

    # Strength evaluation
    if score <= 2:
        return "⚠️ Weak Password"
    elif score <= 4:
        return "👌 Moderate Password"
    else:
        return "✅ Strong Password"

# Demo
if __name__ == "__main__":
    pwd = input("Enter your password to check strength: ")
    print(check_password_strength(pwd))
