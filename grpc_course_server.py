import grpc
from concurrent import futures
import time

# Импортируем сгенерированные модули
import course_service_pb2
import course_service_pb2_grpc


class CourseServiceServicer(course_service_pb2_grpc.CourseServiceServicer):
    """Реализация методов сервиса CourseService."""

    def GetCourse(self, request, context):
        # Формируем ответ на основе полученных данных
        return course_service_pb2.GetCourseResponse(
            course_id=request.course_id,
            title="Автотесты API",
            description="Будем изучать написание API автотестов"
        )


def serve():
    # Создаем gRPC-сервер с пулом потоков
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # Регистрируем наш сервис в сервере
    course_service_pb2_grpc.add_CourseServiceServicer_to_server(
        CourseServiceServicer(), server
    )

    # Указываем порт для прослушивания
    server.add_insecure_port('[::]:50051')

    # Запускаем сервер
    server.start()
    print("gRPC сервер запущен и слушает порт 50051...")

    try:
        # Держим сервер запущенным
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        print("Остановка сервера...")
        server.stop(0)


if __name__ == '__main__':
    serve()