import os
import time

class BlockingFileList:
    def __init__(self, base_directory, expected_file_count=0, extension=".jpg"):
        self.base_directory = base_directory
        self.expected_file_count = expected_file_count
        self.extension = extension

    def __getitem__(self, index):
        file_path = os.path.join(self.base_directory, str(index) + self.extension)
        timeout = 30  # Maximum wait time of 30s
        start_time = time.time()

        while not os.path.exists(file_path):
            waited = time.time() - start_time
            if waited >= timeout:
                raise FileNotFoundError(f"File {file_path} not found after waiting for {timeout} seconds")
            print(f"Could not find file {file_path}. Waiting for it to appear (waited {waited}/{timeout})...")
            time.sleep(1)  # Wait for 1 second before checking again

        return file_path

    def __len__(self):
        return self.expected_file_count