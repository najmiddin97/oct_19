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
    host=creds.host,
    dbname=creds.dbname,
    user=creds.user,
    password=creds.password,
)
cur = conn.cursor()