def ai_classify(content):

    content = content.lower()

    confidential_words = [
        "employee",
        "bank account",
        "credit card",
        "customer",
        "salary",
        "financial report",
        "source code",
        "project x",
        "internal document",
        "secret project"
    ]

    score = 0

    matched_words = []

    for word in confidential_words:
        if word in content:
            score += 1
            matched_words.append(word)

    print("AI MATCHES:", matched_words)

    if score >= 3:
        return "CONFIDENTIAL"

    if score >= 1:
        return "INTERNAL"

    return "PUBLIC"