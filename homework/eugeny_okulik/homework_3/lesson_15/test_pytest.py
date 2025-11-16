import requests
import pytest


def test_new_blogs_create():
    body = {
  "category": "a32934c5-77c9-4617-b533-8d6fd85165c7",
  "name": "Bugungi kunimdan olgan kichik bir saboq",
  "description": "Bugun ertalab odatdagidek shoshilinch boshlandi. Ishlar ko‘pligi, rejalar tig‘izligi biroz charchatdi. Lekin kun davomida bitta narsani angladim: har qanday vaziyatda ham o‘zingni bosib, vazmin bo‘lish juda muhim ekan. Ba’zan kichik bir pauza olib, chuqur nafas olish ham odamni tinchlantirib, to‘g‘ri qaror chiqarishda yordam beradi. Hayot shoshilish haqida emas — his qilish, tushunish va qadrlash haqida ekan. O‘zim uchun kichik, ammo muhim xulosaga keldim: har kuni kamida 5 daqiqa bo‘lsa ham o‘zim uchun vaqt ajratishim kerak.",
  "main_image_url": "https://hikmatlar.uz/quote/1586/generated-img.jpg",
  "images": [
    {
      "image_url": "https://hikmatlar.uz/quote/1586/generated-img.jpg"
    },
    {
      "image_url": "https://hikmatlar.uz/quote/11/generated-img.jpg"
    }
  ],
  "videos": []
}

    token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzY1Nzc5NjQwLCJpYXQiOjE3NjMxODc2NDAsImp0aSI6IjQ4NmE3ZWM0NzY4MzRmOGU5MDNhMTEwNmQzOTUxZGU0IiwidXNlcl9pZCI6IjQ3OTdjYWNlLTJkNDQtNGU5Yi1iMjgyLWUxYzM3NzNjMWRkYiIsImRldmljZV9pZCI6ImUzNDQyY2ZjLWU1NjQtNGFiNy1iMzUxLTFhZTFhNGE5ZmNmMyJ9.T98AG48KHFzYNNHeTzu-U9t3ZgAdLsPKnc4NGV1cPm4'
    headers = {'Content-Type': 'application/json', "Authorization": f"Bearer {token}"}
    response = requests.post(
        'https://api-inextlynk.upgrow.uz/api/v1/profile/blog/posts/',
        json=body,
        headers=headers
    )
    name = response.json()["name"]
    return name




TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzY1Nzc5NjQwLCJpYXQiOjE3NjMxODc2NDAsImp0aSI6IjQ4NmE3ZWM0NzY4MzRmOGU5MDNhMTEwNmQzOTUxZGU0IiwidXNlcl9pZCI6IjQ3OTdjYWNlLTJkNDQtNGU5Yi1iMjgyLWUxYzM3NzNjMWRkYiIsImRldmljZV9pZCI6ImUzNDQyY2ZjLWU1NjQtNGFiNy1iMzUxLTFhZTFhNGE5ZmNmMyJ9.T98AG48KHFzYNNHeTzu-U9t3ZgAdLsPKnc4NGV1cPm4'
HEADERS = {'Content-Type': 'application/json', "Authorization": f"Bearer {TOKEN}"}


@pytest.fixture()
def get_blog_post_slug():
    response = requests.get(
        "https://api-inextlynk.upgrow.uz/api/v1/profile/blog/posts/",
        headers=HEADERS
    ).json()

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






#
#
# @pytest.mark.skip('Testga tayyor emas tez ozgartiriladigan bolim')
# def test_get_all_posts():
#     response = requests.get('https://api-inextlynk.upgrow.uz/api/v1/marketplace/home-page-product-categories/?page=1').json()
#     assert response["count"] == 23
#
#
#
# def test_one_post():
#     slug = 'sement-xaridi-uchun-yetkazib-beruvchi-izlanmoqda'
#     response = requests.get(f'https://api-inextlynk.upgrow.uz/api/v1/marketplace/list/{slug}').json()
#     assert response["slug"] == slug
#
#
#
# def test_get_blogs():
#     token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzY1Nzc5NjQwLCJpYXQiOjE3NjMxODc2NDAsImp0aSI6IjQ4NmE3ZWM0NzY4MzRmOGU5MDNhMTEwNmQzOTUxZGU0IiwidXNlcl9pZCI6IjQ3OTdjYWNlLTJkNDQtNGU5Yi1iMjgyLWUxYzM3NzNjMWRkYiIsImRldmljZV9pZCI6ImUzNDQyY2ZjLWU1NjQtNGFiNy1iMzUxLTFhZTFhNGE5ZmNmMyJ9.T98AG48KHFzYNNHeTzu-U9t3ZgAdLsPKnc4NGV1cPm4'
#     headers = {
#         "Authorization": f"Bearer {token}"
#     }
#     response = requests.get("https://api-inextlynk.upgrow.uz/api/v1/profile/blog/posts/", headers=headers).json()
#     assert response["count"] == 14