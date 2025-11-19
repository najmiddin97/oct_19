import pytest
import requests
import payloads
import endpoints

BASE_URL = "https://api-inextlynk.upgrow.uz/api/v1"

def test_new_blogs_create(get_token):
    # Tokenni HEADERS ichiga joylash
    headers = {'Content-Type': 'application/json', "Authorization": f"Bearer {get_token}"}
    url = f"{BASE_URL}{endpoints.profile_blog_posts}"
    body = payloads.blog_body
    response = requests.post(url, json=body, headers=headers)
    assert response.status_code == 201, f"Expected 201, got {response.status_code}"






def test_get_blogs_slug(get_blog_post_slug, get_token):
    headers = {'Content-Type': 'application/json', "Authorization": f"Bearer {get_token}"}
    response = requests.get(f"{BASE_URL}{endpoints.profile_blog_posts}{get_blog_post_slug}",headers=headers).json()
    assert response["slug"] == get_blog_post_slug








@pytest.mark.skip('Testga tayyor emas tez ozgartiriladigan bolim')
def test_get_all_posts():
    url = f"{BASE_URL}/marketplace/home-page-product-categories/?page=1"
    response = requests.get(url, headers=HEADERS).json()
    assert response["count"] == 23




#profile listda bloglar soni tekshirish
def test_get_blogs(get_token):
    url = f"{BASE_URL}{endpoints.profile_blog_posts}"
    headers = {'Content-Type': 'application/json', "Authorization": f"Bearer {get_token}"}
    response = requests.get(url, headers=headers).json()
    assert response["count"] == 21





def test_profile_blog_post_partial_update(get_token, get_blog_post_slug):
    url = f"{BASE_URL}{endpoints.profile_blog_posts}{get_blog_post_slug}/"
    body = payloads.patch_blog_body
    headers = {'Content-Type': 'application/json', "Authorization": f"Bearer {get_token}"}
    response = requests.patch(url, json=body, headers=headers)

    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    # Agar server JSON qaytsa:
    try:
        data = response.json()
        assert data["name"] == body["name"]
        assert data["description"] == body["description"]
    except ValueError:
        print("Response is not JSON")
