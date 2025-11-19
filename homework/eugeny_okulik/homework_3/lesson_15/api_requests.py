import requests

def all_posts():
    response = requests.get(
        'https://api-inextlynk.upgrow.uz/api/v1/marketplace/home-page-product-categories/?page=1'
    )
    # Status code assert
    assert response.status_code == 200
    data = response.json()

    # Main keys assert
    assert "count" in data
    assert "results" in data
    assert isinstance(data["results"], list)

    # Optional: har bir category elementini tekshirish
    for category in data["results"]:
        assert "id" in category
        assert "name" in category
        assert "icon_url" in category
        assert "information_data" in category
        assert isinstance(category["information_data"], list)

    # JSON ma’lumotini chiqarish
    print(data)







def one_post():
    slug = 'sement-xaridi-uchun-yetkazib-beruvchi-izlanmoqda'
    response = requests.get(f'https://api-inextlynk.upgrow.uz/api/v1/marketplace/list/{slug}/').json()
    assert response["name"] == "Looking for a supplier for cement purchase", 'case failed'






def post_a_post():
    body = {
        "category": "a32934c5-77c9-4617-b533-8d6fd85165c7",
        "name": "Килиан Мбаппе представлен в качестве игрока «Реал Мадрид»",
        "description": "Французский нападающий Килиан Мбаппе официально стал игроком мадридского «Реала». 26-летний форвард подписал контракт до 2031 года. На презентации на «Сантьяго Бернабеу» Мбаппе заявил: «Сегодня сбывается моя мечта. С детства я мечтал играть в этом клубе, носить эту футболку и выступать перед болельщиками «Реала». Спасибо моему бывшему клубу «ПСЖ» за все эти годы и за поддержку. Теперь начинается новый этап моей карьеры, и я сделаю всё, чтобы приносить радость нашим фанатам и завоевывать новые титулы».",
        "main_image_url": "http://api-inextlynk.upgrow.uz/media/image/2025/10/16/dark_2d794ee296ad4e27.jpg",
        "images": [
            {
                "image_url": "http://api-inextlynk.upgrow.uz/media/image/2025/10/16/dark_2d794ee296ad4e27.jpg"
            }
        ],
        "videos": [
            {
                "video_url": "https://www.youtube.com/watch?v=U7a7a8o4eGQ"
            }
        ]
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post('https://api-inextlynk.upgrow.uz/api/v1/profile/blog/posts/', json=body, headers=headers).json()
    print(response)

all_posts()