import time
import pathlib
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

destinationDirectory = pathlib.Path.home().joinpath('Desktop', 'Destination Folder')

class Watcher:

    directoryToWatch = pathlib.Path.home().joinpath('Desktop', 'Junk Folder')

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.directoryToWatch, recursive=True)
        self.observer.start()
        
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Error")

        self.observer.join()

class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None
        
        elif event.event_type == 'created':
            # take action on created event
            shutil.move(src=event.src_path, dst=destinationDirectory.joinpath(pathlib.Path(event.src_path).name))
            print("Received created event")
            print("Moved file from", pathlib.Path(event.src_path).parent.name, "to", destinationDirectory.name)
        
        elif event.event_type == 'modified':
            # take action on modified event
            print("Received modified event")

if __name__ == '__main__':
    w = Watcher()
    w.run()