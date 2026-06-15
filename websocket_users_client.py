import asyncio
import websockets


async def main():
    """Подключение к серверу, отправка сообщения и получение 5 ответов."""
    async with websockets.connect("ws://localhost:8765") as websocket:
        # Отправляем одно сообщение серверу
        await websocket.send("Привет, сервер!")

        # Получаем и выводим 5 ответных сообщений
        for _ in range(5):
            message = await websocket.recv()
            print(message)


if __name__ == "__main__":
    asyncio.run(main())