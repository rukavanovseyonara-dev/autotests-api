import httpx  # Импортируем библиотеку HTTPX

login_payload = {
    "email": "userSA1@example.com",
    "password": "userSA1@example.com"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

print("Login response:", login_response_data)
print("Status Code:", login_response.status_code)

refresh_payload = {
    "refreshToken": login_response_data["token"]["refreshToken"]
}

refresh_response = httpx.post("http://localhost:8000/api/v1/authentication/refresh", json=refresh_payload)
refresh_response_data = refresh_response.json()

print("Refresh response:", refresh_response_data)
print("Status Code:", refresh_response.status_code)

get_user_me_headers = {
    "Authorization": "Bearer " + refresh_response_data["token"]["accessToken"]
}

get_user_me_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=get_user_me_headers)
get_user_me_response_data = get_user_me_response.json()

print("Get user me response:", get_user_me_response_data)
print("Status Code:", get_user_me_response.status_code)



