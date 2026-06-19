import socket
import threading

HOST = "127.0.0.1"
PORT = 12345

messages = []
lock = threading.Lock()


def handle_client(client_socket, address):
    print(f"Пользователь с адресом: {address} подключился к серверу")

    try:
        data = client_socket.recv(1024).decode().strip()

        print(f"Пользователь с адресом: {address} отправил сообщение: {data}")

        with lock:
            messages.append(data)
            history = "\n".join(messages)

        client_socket.send(history.encode())

    except Exception as e:
        print(f"Ошибка с клиентом {address}: {e}")

    finally:
        client_socket.close()


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(10)

    print(f"Сервер запущен на {HOST}:{PORT}")

    while True:
        client_socket, address = server.accept()
        thread = threading.Thread(
            target=handle_client,
            args=(client_socket, address),
            daemon=True
        )
        thread.start()


if __name__ == "__main__":
    main()