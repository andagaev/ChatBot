import os

from src import tg

file_path = os.environ["FILE_PATH"]


def main():
    message = read_from_file(file_path)
    tg.send_message_to_Telegram(message_to_send=message)


def read_from_file(path: str) -> str:
    try:
        with open(path, "r") as f:
            return f.read()
    except FileNotFoundError as e:
        return f"Error occured: {e}"


if __name__ == "__main__":
    main()
