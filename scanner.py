import re

PAN_REGEX = r"[A-Z]{5}[0-9]{4}[A-Z]"
AADHAAR_REGEX = r"\b\d{12}\b"
EMAIL_REGEX = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"

KEYWORDS = [
    "confidential",
    "secret",
    "internal use only",
    "do not share",
    "salary",
    "customer database",
    "api_key",
    "password"
]


def scan_content(content):
    findings = []

    if re.search(PAN_REGEX, content):
        findings.append("PAN")

    if re.search(AADHAAR_REGEX, content):
        findings.append("AADHAAR")

    if re.search(EMAIL_REGEX, content):
        findings.append("EMAIL")

    content_lower = content.lower()

    for keyword in KEYWORDS:
        if keyword.lower() in content_lower:
            findings.append("KEYWORD")
            break

    return findings