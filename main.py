import os
import time
import shutil

from scanner import scan_content
from classifier import classify
from logger import log_incident
from database import init_db, save_incident
from file_reader import read_file
from ai_classifier import ai_classify

MONITOR_DIR = "monitored"
QUARANTINE_DIR = "quarantine"

seen = set()

os.makedirs(MONITOR_DIR, exist_ok=True)
os.makedirs(QUARANTINE_DIR, exist_ok=True)

init_db()

print("================================")
print("DLP Agent Running...")
print("Monitoring:", os.path.abspath(MONITOR_DIR))
print("================================")


while True:

    try:

        for filename in os.listdir(MONITOR_DIR):

            filepath = os.path.join(
                MONITOR_DIR,
                filename
            )

            if filepath in seen:
                continue

            seen.add(filepath)

            print(f"\n[NEW FILE] {filename}")

            content = read_file(filepath)

            if not content:
                print("Unable to read file")
                continue

            findings = scan_content(content)

            print(
                "FINDINGS:",
                findings if findings else "None"
            )

            if findings:

                classification = classify(findings)

            else:

                classification = ai_classify(content)

            if classification == "RESTRICTED":

                action = "QUARANTINE"

            elif classification == "CONFIDENTIAL":

                action = "BLOCK"

            elif classification == "INTERNAL":

                action = "WARN"

            else:

                action = "ALLOW"

            print(
                "CLASSIFICATION:",
                classification
            )

            print(
                "ACTION:",
                action
            )

            log_incident(
                filename,
                classification,
                action
            )

            save_incident(
                filename,
                classification,
                action
            )

            if action == "QUARANTINE":

                destination = os.path.join(
                    QUARANTINE_DIR,
                    filename
                )

                try:

                    shutil.move(
                        filepath,
                        destination
                    )

                    print(
                        f"[QUARANTINED] {filename}"
                    )

                except Exception as e:

                    print(
                        f"Quarantine Error: {e}"
                    )

        time.sleep(2)

    except KeyboardInterrupt:

        print("\nDLP Agent Stopped")
        break

    except Exception as e:

        print("ERROR:", e)