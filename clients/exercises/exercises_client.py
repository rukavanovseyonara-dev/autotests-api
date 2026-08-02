from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient
from clients.private_http_builder import get_private_http_client


class Exercise(TypedDict):
    """
    Описание структуры упражнения.
    """
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class GetExercisesQueryDict(TypedDict):
    """
    Описание структуры запроса на получение списка упражнений.
    """
    courseId: str


class GetExercisesResponseDict(TypedDict):
    exercises: list[Exercise]


class GetExerciseResponseDict(TypedDict):
    exercise: Exercise


class CreateExercisesRequestDict(TypedDict):
    """
    Описание структуры запроса на создание упражнения.
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class CreateExerciseResponseDict(TypedDict):
    exercise: Exercise


class UpdateExercisesRequestDict(TypedDict):
    """
    Описание структуры запроса на обновление упражнения.
    """
    title: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class UpdateExerciseResponseDict(TypedDict):
    exercise: Exercise


class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """

    # -------- API методы --------

    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """
        Метод получения списка упражнений (сырой Response).
        """
        return self.get("/api/v1/exercises", params=query)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения упражнения (сырой Response).
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request: CreateExercisesRequestDict) -> Response:
        """
        Метод создания упражнения (сырой Response).
        """
        return self.post("/api/v1/exercises", json=request)

    def update_exercise_api(self, exercise_id: str, request: UpdateExercisesRequestDict) -> Response:
        """
        Метод обновления упражнения (сырой Response).
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления упражнения (сырой Response).
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")

    # -------- Бизнес методы --------

    def get_exercises(self, query: GetExercisesQueryDict) -> GetExercisesResponseDict:
        """
        Метод получения списка упражнений.

        :param query: Словарь с courseId.
        :return: JSON-ответ с упражнениями.
        """
        response = self.get_exercises_api(query)
        return response.json()

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseDict:
        """
        Метод получения упражнения.

        :param exercise_id: Идентификатор упражнения.
        :return: JSON-ответ с упражнением.
        """
        response = self.get_exercise_api(exercise_id)
        return response.json()

    def create_exercise(self, request: CreateExercisesRequestDict) -> CreateExerciseResponseDict:
        """
        Метод создания упражнения.

        :param request: Данные для создания упражнения.
        :return: JSON-ответ с упражнением.
        """
        response = self.create_exercise_api(request)
        return response.json()

    def update_exercise(self, exercise_id: str, request: UpdateExercisesRequestDict) -> UpdateExerciseResponseDict:
        """
        Метод обновления упражнения.

        :param exercise_id: Идентификатор упражнения.
        :param request: Данные для обновления.
        :return: JSON-ответ с упражнением.
        """
        response = self.update_exercise_api(exercise_id, request)
        return response.json()


def get_exercises_client() -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с авторизацией.

    :return: Готовый ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client())