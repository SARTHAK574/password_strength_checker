import re

# Sample list of common passwords
COMMON_PASSWORDS = {
    "123456", "password", "123456789", "12345678", "qwerty", "abc123",
    "111111", "123123", "admin", "letmein", "welcome", "password1"
}

def check_password_strength(password):
    score = 0
    feedback = []

    # Length score
    length = len(password)
    if length < 8:
        feedback.append("Password is too short. Use at least 8 characters.")
    elif 8 <= length < 12:
        score += 10
        feedback.append("Good length. Consider making it longer.")
    else:
        score += 25
        feedback.append("Great! Your password length is strong.")

    # Character variety
    has_lower = re.search(r"[a-z]", password) is not None
    has_upper = re.search(r"[A-Z]", password) is not None
    has_digit = re.search(r"[0-9]", password) is not None
    has_special = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is not None

    variety_score = sum([has_lower, has_upper, has_digit, has_special]) * 15
    score += variety_score

    if not has_lower:
        feedback.append("Add lowercase letters.")
    if not has_upper:
        feedback.append("Add uppercase letters.")
    if not has_digit:
        feedback.append("Add numbers.")
    if not has_special:
        feedback.append("Add special characters (!@#$ etc).")

    # Common password check
    if password.lower() in COMMON_PASSWORDS:
        feedback.append("This is a commonly used password. Choose a more unique one.")
        score -= 30

    # Repeating characters or sequences
    if re.search(r"(.)\1{2,}", password):
        feedback.append("Avoid repeating characters (like aaa or 111).")
        score -= 10

    # Final scoring clamp
    score = max(0, min(score, 100))
    
    # Strength classification
    if score < 40:
        strength = "Weak"
    elif 40 <= score < 70:
        strength = "Moderate"
    else:
        strength = "Strong"

    return score, strength, feedback


# ---------- CLI Interface ----------
if __name__ == "__main__":
    print("🔐 Password Strength Checker 🔐")
    password = input("Enter a password to analyze: ").strip()
    score, strength, feedback = check_password_strength(password)

    print(f"\nPassword Strength: {strength}")
    print(f"Score: {score}/100")
    print("Feedback:")
    for line in feedback:
        print(f" - {line}")
