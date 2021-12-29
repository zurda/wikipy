import click.testing
import pytest
from wikipy import console


@pytest.fixture
def runner():
    return click.testing.CliRunner()


@pytest.fixture
def mock_requests_get(mocker):
    mock = mocker.patch("requests.get")
    mock.return_value.__enter__.return_value.json.return_value = {
        "title": "Lorem Ipsum",
        "extract": "Lorem ipsum dolor sit amet",
    }
    return mock


def test_main_succeeds(runner):
    result = runner.invoke(console.main)
    assert result.exit_code == 0


def test_main_prints_title(runner, mock_requests_get):
    result = runner.invoke(console.main)
    assert "Lorem Ipsum" in result.output


def test_main_prints_extract(runner, mock_requests_get):
    result = runner.invoke(console.main)
    assert "Lorem ipsum dolor sit amet" in result.output


def test_main_invokes_requests_get(runner, mock_requests_get):
    runner.invoke(console.main)
    assert mock_requests_get.called


def test_main_with_title_argument(runner):
    result = runner.invoke(console.main, ["The Office"])
    assert result.exit_code == 0
    assert not result.exception
    assert "mockumentary sitcom" in result.output
