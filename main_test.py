import main
import sys


def test_read_from_file_success(mocker):
    # Arrange
    mock_open = mocker.mock_open(read_data="mocked content")
    mocker.patch("builtins.open", mock_open)

    # Act
    result = main.read_from_file("./test.txt")

    # Assert
    assert result == "mocked content"


def test_read_from_file_fail():
    # Act
    result = main.read_from_file("wrong path")

    # Assert
    assert result == "Error occured: [Errno 2] No such file or directory: 'wrong path'"


def test_get_file_path_success(mocker):
    passed_arg = "test_arg"
    mocker.patch.object(sys, "argv", ["main.py", passed_arg])

    result = main.get_file_path()
    assert result == passed_arg


def test_get_file_path_fail(mocker):
    mocker.patch.object(sys, "argv", ["main.py"])

    result = main.get_file_path()
    assert result == "File path is not provided, please provide file path"
