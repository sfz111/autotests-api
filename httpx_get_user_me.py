import httpx

login_payload = {
    "email": "sfz111@mail.ru",
    "password": "string"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

print("Login response:", login_response_data)
print("Login status code:", login_response.status_code)

get_user_headers = {f"Authorization": f"Bearer {login_response_data['token']['accessToken']}"}
get_user_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=get_user_headers)
get_user_response_data = get_user_response.json()
print("Get user response:", get_user_response_data)
print("Get user status code:", get_user_response.status_code)
