import grpc

# Импортируем сгенерированные модули
import course_service_pb2
import course_service_pb2_grpc


def run():
    # Устанавливаем небезопасное соединение с сервером на localhost:50051
    with grpc.insecure_channel('localhost:50051') as channel:
        # Создаем stub (заглушку) для вызова методов сервиса
        stub = course_service_pb2_grpc.CourseServiceStub(channel)

        # Формируем запрос GetCourseRequest
        request = course_service_pb2.GetCourseRequest(course_id="api-course")

        # Вызываем метод GetCourse и получаем ответ
        response = stub.GetCourse(request)

        # Выводим полученный ответ в консоль
        print(response)


if __name__ == '__main__':
    run()