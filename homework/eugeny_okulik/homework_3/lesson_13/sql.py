import psycopg2
import uuid
from datetime import datetime, UTC
import re
import creds


def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')

conn = psycopg2.connect(
    host="localhost",
    dbname="inexlynk_local",
    user="postgres",
    password="1234"
)
cur = conn.cursor()

post_id = str(uuid.uuid4())
created_time = datetime.now(UTC)
name = 'Post for Testing!'
slug = slugify(name)

# ❗ foydalanuvchi id sini bazadan olish (masalan birinchi foydalanuvchi)
cur.execute("SELECT id FROM auth_user LIMIT 1;")
user_row = cur.fetchone()
if not user_row:
    raise ValueError("Bazaga post kiritish uchun avval foydalanuvchi kerak!")
user_id = user_row[0]

query = """
INSERT INTO blog_post ("id", "created_at", "is_archive", "name", "description", "main_image_url", "slug", "user_id")
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
RETURNING "id";
"""
cur.execute(query, (
    post_id,
    created_time,
    False,
    name,
    'Bu test uchun yozilgan post.',
    'https://example.com/default-image.jpg',
    slug,
    user_id
))
new_id = cur.fetchone()[0]
conn.commit()

print(f"✅ Post yaratildi: {new_id}\n👤 User ID: {user_id}\n🔗 Slug: {slug}")

cur.close()
conn.close()
