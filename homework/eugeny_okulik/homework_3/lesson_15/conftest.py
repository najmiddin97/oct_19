import pytest
import requests
import payloads
import endpoints

BASE_URL = "https://api-inextlynk.upgrow.uz/api/v1"


@pytest.fixture()
def get_token():
    url = f"{BASE_URL}{endpoints.login_emile}"
    payload = payloads.login_me
    response = requests.post(url, json=payload)
    assert response.status_code == 200, f"Login failed: {response.text}"
    return response.json().get("access_token")


@pytest.fixture()
def get_another_token():
    url = f"{BASE_URL}{endpoints.login_emile}"
    payload = payloads.login_another
    response = requests.post(url, json=payload)
    assert response.status_code == 200, f"Login failed: {response.text}"
    return response.json().get("access_token")




@pytest.fixture()
def get_blog_post_slug(get_token):
    url = f"{BASE_URL}{endpoints.profile_blog_posts}"
    headers = {'Content-Type': 'application/json', "Authorization": f"Bearer {get_token}"}
    response = requests.get(url, headers=headers).json()
    results = response.get("results")
    slug = results[0]["slug"]
    return slug


    # # Teardown: blogni archive qilamiz
    # archive_url = f"{BASE_URL}{endpoints.profile_blog_posts}{slug}/archive/"
    # archive_resp = requests.patch(archive_url, headers=headers)
    # print(f' Archived post slug: {slug}, status: {archive_resp.status_code}')
    #
    # # Teardown: blogni delete qilamiz
    # delete_url = f"{BASE_URL}{endpoints.profile_blog_posts}{slug}/"
    # delete_resp = requests.delete(delete_url, headers=headers)
    # print(f'Deleted post slug: {slug}, status: {delete_resp.status_code}')