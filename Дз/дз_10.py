import requests
import sqlite3
from bs4 import BeautifulSoup
from datetime import datetime

conn = sqlite3.connect("weather_DB.sl3")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS weather (datetime TEXT,temperature INTEGER)")
url = "https://sinoptik.ua/pohoda/mykolaiv"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers, timeout=10)
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")
temp_tag = soup.select_one("p.R1ENpvZz")
temperature = int(
    temp_tag.text.replace("°C", "").replace("+", "").strip()
)
now = datetime.now().strftime("%Y-%m-%d %H:%M")
cur.execute("INSERT INTO weather (datetime, temperature) VALUES (?, ?)",(now, temperature))
conn.commit()
cur.execute("SELECT rowid, datetime, temperature FROM weather")
print(cur.fetchall())
conn.close()