"""Task 1: Password Strength Checker"""
import re

COMMON = {"password", "123456", "12345678", "qwerty", "abc123",
          "letmein", "admin", "welcome", "iloveyou", "password1"}


def check_password(pw):
    score, tips = 0, []

    if len(pw) >= 12:
        score += 2
    elif len(pw) >= 8:
        score += 1
        tips.append("Use 12+ characters.")
    else:
        tips.append("Too short: use at least 8 characters.")

    checks = [
        (r"[a-z]", "Add lowercase letters."),
        (r"[A-Z]", "Add uppercase letters."),
        (r"\d", "Add numbers."),
        (r"[^A-Za-z0-9]", "Add special characters (!@#$...)."),
    ]
    for pattern, tip in checks:
        if re.search(pattern, pw):
            score += 1
        else:
            tips.append(tip)

    if pw.lower() in COMMON:
        score = 0
        tips.append("This is a very common password. Avoid it.")
    if re.search(r"(.)\1{2,}", pw):
        score -= 1
        tips.append("Avoid repeating the same character 3+ times.")

    score = max(score, 0)
    if score <= 2:
        level = "Weak"
    elif score <= 4:
        level = "Medium"
    else:
        level = "Strong"
    return level, score, tips


if __name__ == "__main__":
    while True:
        pw = input("\nEnter a password (or 'q' to quit): ")
        if pw.lower() == "q":
            break
        level, score, tips = check_password(pw)
        print(f"Strength: {level} (score {score}/6)")
        for t in tips:
            print(" -", t)
