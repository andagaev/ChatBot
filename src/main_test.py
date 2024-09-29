from src import main


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
