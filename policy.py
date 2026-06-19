def get_action(classification):

    policies = {
        "PUBLIC": "ALLOW",
        "INTERNAL": "WARN",
        "CONFIDENTIAL": "BLOCK",
        "RESTRICTED": "QUARANTINE"
    }

    return policies.get(classification, "ALLOW")