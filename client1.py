import socket
import threading

PORT = 5050
SERVER = "localhost"
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"


def receive_messages(client):
    """Handle incoming messages from the server."""
    while True:
        try:
            msg = client.recv(1024).decode(FORMAT)
            print(f"Broadcast: {msg}")
        except:
            print("An error occurred. Disconnected from server.")
            client.close()
            break


def connect():
    """Create a client socket and connect to the server."""
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    return client


def send(client, msg):
    """Send a message to the server."""
    message = msg.encode(FORMAT)
    client.send(message)


def start():
    client = connect()
    
    # Start a thread to handle receiving messages
    thread = threading.Thread(target=receive_messages, args=(client,))
    thread.start()

    while True:
        msg = input("Message (q for quit): ")

        if msg.lower() == 'q':
            send(client, DISCONNECT_MESSAGE)
            break

        send(client, msg)


start()
