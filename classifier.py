def classify(findings):

    if "AADHAAR" in findings:
        return "RESTRICTED"

    if "PAN" in findings:
        return "CONFIDENTIAL"

    if "KEYWORD" in findings:
        return "CONFIDENTIAL"

    if "EMAIL" in findings:
        return "INTERNAL"

    return "PUBLIC"