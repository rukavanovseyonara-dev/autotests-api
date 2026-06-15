import asyncio
import websockets


async def handler(websocket):
    """Обработчик подключений: принимает сообщения и отправляет 5 ответов."""
    async for message in websocket:
        # Логируем полученное сообщение
        print(f"Получено сообщение от пользователя: {message}")

        # Отправляем 5 ответных сообщений
        for i in range(1, 6):
            await websocket.send(f"{i} Сообщение пользователя: {message}")


async def main():
    """Запуск сервера на localhost:8765."""
    async with websockets.serve(handler, "localhost", 8765):
        print("WebSocket-сервер запущен на ws://localhost:8765")
        await asyncio.Future()  # работать бесконечно


if __name__ == "__main__":
    asyncio.run(main())