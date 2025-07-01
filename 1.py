import socket
import threading

HOST = '0.0.0.0'  # Listen on all available interfaces
PORT = 1234

def handle_client(conn, addr):
    print(f"[+] Accepted connection from {addr[0]}:{addr[1]}")
    try:
        while True:
            command = input("Shell> ")
            if command.lower() in ('exit', 'quit'):
                conn.sendall(b"exit") # Send exit to client to terminate its loop
                break
            if not command:
                continue

            conn.sendall(command.encode())
            response = conn.recv(4096) # Increased buffer size
            print(response.decode(errors='ignore'), end='') # end='' to avoid double newline
    except Exception as e:
        print(f"[-] Error handling client {addr[0]}:{addr[1]}: {e}")
    finally:
        print(f"[-] Connection from {addr[0]}:{addr[1]} closed")
        conn.close()

def start_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Allow address reuse
    try:
        s.bind((HOST, PORT))
        s.listen(1) # Listen for one connection
        print(f"[*] Listening on {HOST}:{PORT}")

        conn, addr = s.accept()
        handle_client(conn, addr)

    except Exception as e:
        print(f"[-] Server error: {e}")
    finally:
        s.close()

if __name__ == "__main__":
    start_server()
