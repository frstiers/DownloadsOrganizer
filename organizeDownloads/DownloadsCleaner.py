import time
import pathlib
import shutil

from extensions import extension_paths

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

destinationDirectory = pathlib.Path.home().joinpath('Documents', 'Organized Downloads')

class Watcher:

    directoryToWatch = pathlib.Path.home().joinpath('Downloads')

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.directoryToWatch, recursive=True)
        self.observer.start()
        
        try:
            while True:
                time.sleep(30)
        except:
            self.observer.stop()
            print("Error")

        self.observer.join()

def renameFile(source: pathlib.Path, destinationPath: pathlib.Path):
    if pathlib.Path(destinationPath / source.name).exists():
            increment = 0
            
            while True:
                increment += 1
                newName = destinationPath / f'{source.stem}_{increment}{source.suffix}'

                if not newName.exists():
                    return newName
    else:
        return pathlib.Path(destinationPath / source.name)

class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None
        
        elif event.event_type == 'created':
            # Take action on created event
            
            print("Received created event")

            thisFile = pathlib.Path(event.src_path)

            if thisFile.is_file() and thisFile.suffix.lower() in extension_paths:
                newDestination = destinationDirectory.joinpath(extension_paths[thisFile.suffix.lower()], thisFile.name)
                newDestination = renameFile(source=thisFile, destinationPath=newDestination.parent)
                shutil.move(src=event.src_path, dst=newDestination)

                print("Moved file from", pathlib.Path(event.src_path).parent.name, "to", newDestination.parent.name)

        # Uncomment this to start doing things when files are modified in the watched directory.
        # elif event.event_type == 'modified':
        #     # take action on modified event
        #     print("Received modified event")

if __name__ == '__main__':
    w = Watcher()
    w.run()