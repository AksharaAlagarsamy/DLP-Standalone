from datetime import datetime


def log_incident(filename, classification, action):

    with open("incidents.log", "a") as f:

        f.write(
            f"{datetime.now()} | "
            f"{filename} | "
            f"{classification} | "
            f"{action}\n"
        )