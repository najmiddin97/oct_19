import pytest
import requests
from faker import Faker
fake = Faker(locale='ru_RU')

BASE_URL = "https://api-inextlynk.upgrow.uz/api/v1"
DEVICE_INFO = {
    "device_id": "e3980453-e09a-439a-b165-4d9e5518e4eb",
    "firebase_token": "string",
    "platform": "android",
    "os_version": "string",
    "device_model": "string",
    "location": "string"
}

@pytest.mark.parametrize(
    "email,password,expected_status",
    [
        ("nurimen738@gmail.com", "1", 200),   # success
        (fake.email(), "Qwerty1@", 400), # fail
        (fake.email(), "qwerty1@", 400),  #fail
        (fake.email(), "qwerty1@", 400),  # fail
        (fake.email(), "Qwerty1@", 400),  # fail
        (fake.email(), "qWerty1@", 400)   # fail
    ]
)



@pytest.mark.smoke
def test_login_email(email, password, expected_status):
    url = f"{BASE_URL}/auth/login/email/"
    payload = {
        "device": DEVICE_INFO,
        "email": email,
        "password": password
    }

    response = requests.post(url, json=payload)
    assert response.status_code == expected_status, f"Login test failed for {email}"

    if response.status_code == 200:
        data = response.json()
        assert "access_token" in data or "user_id" in data, f"No token returned for {email}"
        print(f"Login successful for: {email}")
    else:
        print(f"Login failed as expected for: {email}")
