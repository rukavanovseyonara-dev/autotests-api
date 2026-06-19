import socket

HOST = "127.0.0.1"
PORT = 12345


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.connect((HOST, PORT))

    message = "Привет, сервер!"
    client.send(message.encode())

    response = client.recv(1024).decode()
    print(response)

    client.close()


if __name__ == "__main__":
    main()