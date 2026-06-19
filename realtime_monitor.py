from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

class DLPHandler(FileSystemEventHandler):

    def on_created(self, event):

        if event.is_directory:
            return

        print(f"\n[REALTIME DETECTED] {event.src_path}")

        # Call DLP scan here
        # process_file(event.src_path)

observer = Observer()

observer.schedule(
    DLPHandler(),
    path="monitored",
    recursive=False
)

observer.start()

print("Realtime DLP Running...")

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    observer.stop()

observer.join()