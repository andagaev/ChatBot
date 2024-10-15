import logging
import os
import threading

from src.queue import emit_message, worker

file_path = os.environ["FILE_PATH"]


def main():
    lines = read_from_file(file_path)

    if not lines:
        logging.error("No messages found to send.")
        return

    worker_thread = threading.Thread(target=worker.start_worker)
    worker_thread.start()

    for message in lines:
        emit_message.send_message_to_queue(message=message)

    worker_thread.join()


def read_from_file(path: str) -> str:
    try:
        with open(path, "r") as f:
            return f.readlines()
    except FileNotFoundError as e:
        return f"Error occured: {e}"


if __name__ == "__main__":
    main()
