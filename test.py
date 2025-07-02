import subprocess
import sys

def run_script_1():
    """
    Executes the script '1.py' using the Python interpreter and checks its output.
    """
    try:
        # Ensure we are using the same Python interpreter that is running test.py
        python_executable = sys.executable
        process_result = subprocess.run(
            [python_executable, '1.py'],
            capture_output=True,
            text=True,
            check=False  # Handle non-zero exit codes manually
        )

        if process_result.returncode == 0:
            print("1.py executed successfully.")
            if process_result.stdout:
                print("Stdout from 1.py:")
                print(process_result.stdout)
        else:
            print(f"1.py execution failed with return code: {process_result.returncode}")
            if process_result.stderr:
                print("Stderr from 1.py:")
                print(process_result.stderr)
            if process_result.stdout: # Also print stdout in case of failure, it might contain useful info
                print("Stdout from 1.py (on failure):")
                print(process_result.stdout)

    except FileNotFoundError:
        print(f"Error: The script '1.py' was not found in the current directory.")
    except Exception as e:
        print(f"An unexpected error occurred while trying to run 1.py: {e}")

if __name__ == "__main__":
    run_script_1()
