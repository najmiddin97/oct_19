import requests
import pytest
from faker import Faker
fake = Faker(locale='ru_RU')

BASE_URL = "https://api-inextlynk.upgrow.uz/api/v1"
TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzY1Nzc5NjQwLCJpYXQiOjE3NjMxODc2NDAsImp0aSI6IjQ4NmE3ZWM0NzY4MzRmOGU5MDNhMTEwNmQzOTUxZGU0IiwidXNlcl9pZCI6IjQ3OTdjYWNlLTJkNDQtNGU5Yi1iMjgyLWUxYzM3NzNjMWRkYiIsImRldmljZV9pZCI6ImUzNDQyY2ZjLWU1NjQtNGFiNy1iMzUxLTFhZTFhNGE5ZmNmMyJ9.T98AG48KHFzYNNHeTzu-U9t3ZgAdLsPKnc4NGV1cPm4'
HEADERS = {'Content-Type': 'application/json', "Authorization": f"Bearer {TOKEN}"}


def test_new_blogs_create():
    url = f"{BASE_URL}/profile/blog/posts/"

    body = {
        "category": "a32934c5-77c9-4617-b533-8d6fd85165c7",  # APIdagi valid UUID
        "name": fake.sentence(nb_words=5),  # qisqa blog title
        "description": "Bugun sodda test blog yaratyapmiz, hech qanday xavf yoki zo‘ravonlik mavjud emas.",  # 3 gapli description
        "main_image_url": "https://via.placeholder.com/150",  # test uchun placeholder image
        "images": [
            {"image_url": "https://via.placeholder.com/150"},
            {"image_url": "https://via.placeholder.com/200"}
        ],
        "videos": [
            {"video_url": "https://sample-videos.com/video123/mp4/240/big_buck_bunny_240p_1mb.mp4"}
        ]
    }

    response = requests.post(url, json=body, headers=HEADERS)

    print(response.status_code)
    print(response.text)

    # Status kodni tekshirish
    assert response.status_code == 201, f"Expected 201, got {response.status_code}"

    # Response ichidagi name tekshirish
    response_data = response.json()
    assert response_data["name"] == body["name"], "Blog name does not match"




@pytest.fixture()
def get_blog_post_slug():
    url = f"{BASE_URL}/profile/blog/posts/"
    response = requests.get(url, headers=HEADERS).json()
    results = response.get("results")
    slug = results[0]["slug"]
    yield slug

    # Teardown: blogni archive va delete qilamiz
    archive_url = f"https://api-inextlynk.upgrow.uz/api/v1/profile/blog/posts/{slug}/archive/"
    delete_url = f"https://api-inextlynk.upgrow.uz/api/v1/profile/blog/posts/{slug}/"

    archive_resp = requests.patch(archive_url, headers=HEADERS)
    print(f' Archived post slug: {slug}, status: {archive_resp.status_code}')

    delete_resp = requests.delete(delete_url, headers=HEADERS)
    print(f'Deleted post slug: {slug}, status: {delete_resp.status_code}')


def test_get_blogs_slug(get_blog_post_slug):
    response = requests.get(
        f"https://api-inextlynk.upgrow.uz/api/v1/profile/blog/posts/{get_blog_post_slug}",
        headers=HEADERS
    ).json()

    assert response["slug"] == get_blog_post_slug








@pytest.mark.skip('Testga tayyor emas tez ozgartiriladigan bolim')
def test_get_all_posts():
    url = f"{BASE_URL}/marketplace/home-page-product-categories/?page=1"
    response = requests.get(url, headers=HEADERS).json()
    assert response["count"] == 23



def test_one_post():
    slug = 'sement-xaridi-uchun-yetkazib-beruvchi-izlanmoqda'
    url = f"{BASE_URL}/marketplace/list/{slug}"
    response = requests.get(url, headers=HEADERS).json()
    assert response["slug"] == slug



def test_get_blogs():
    url = f"{BASE_URL}/profile/blog/posts/"
    response = requests.get(url, headers=HEADERS).json()
    assert response["count"] == 9