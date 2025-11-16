import unittest
import requests


class TestPostApi(unittest.TestCase):
    def test_get_all_posts(self):
        response = requests.get('https://api-inextlynk.upgrow.uz/api/v1/marketplace/home-page-product-categories/?page=1').json()
        self.assertEqual(response["count"], 24)



    def test_one_post(self):
        slug = 'sement-xaridi-uchun-yetkazib-beruvchi-izlanmoqda'
        response = requests.get(f'https://api-inextlynk.upgrow.uz/api/v1/marketplace/list/{slug}').json()
        self.assertEqual(response["slug"], slug)




