import sys


def main():
    file_path = get_file_path()
    message = read_from_file(file_path)
    print(send_message_to_chat(message=message))


def get_file_path() -> str:
    if len(sys.argv) > 1:
        return sys.argv[1]
    return "File path is not provided, please provide file path"


def read_from_file(path: str) -> str:
    try:
        with open(path, "r") as f:
            return f.read()
    except FileNotFoundError as e:
        return f"Error occured: {e}"


def send_message_to_chat(message: str):
    return f"Hello {message}"


if __name__ == "__main__":
    main()
