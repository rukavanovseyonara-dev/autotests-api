from clients.users.public_users_client import get_public_users_client
from clients.files.files_client import get_files_client
from clients.courses.courses_client import get_courses_client
from clients.exercises.exercises_client import get_exercises_client

from tools.fakers import get_random_email


def main():
    users_client = get_public_users_client()
    files_client = get_files_client()
    courses_client = get_courses_client()
    exercises_client = get_exercises_client()

    # 1. пользователь
    user_data = users_client.create_user({
        "email": get_random_email(),
        "password": "12345678",
        "lastName": "string",
        "firstName": "string",
        "middleName": "string"
    })

    user_id = user_data["user"]["id"]

    # 2. файл
    file_data = files_client.create_file(
        file_path="./testdata/files/image.png",
        directory="courses"
    )

    print(f"Create file data: {file_data}")

    file_id = file_data["file"]["id"]

    # 3. курс
    course_data = courses_client.create_course({
        "title": "Python",
        "maxScore": 100,
        "minScore": 10,
        "description": "Python API course",
        "estimatedTime": "2 weeks",
        "previewFileId": file_id,
        "createdByUserId": user_id
    })

    print(f"Create course data: {course_data}")

    course_id = course_data["course"]["id"]

    # 4. упражнение
    exercise_data = exercises_client.create_exercise({
        "title": "Exercise 1",
        "courseId": course_id,
        "maxScore": 5,
        "minScore": 1,
        "orderIndex": 0,
        "description": "Exercise 1",
        "estimatedTime": "5 minutes"
    })

    print(f"Create exercise data: {exercise_data}")


if __name__ == "__main__":
    main()