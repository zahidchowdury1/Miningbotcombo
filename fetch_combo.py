import requests
import json
from bs4 import BeautifulSoup
from datetime import datetime

url = "https://miningcombo.com"
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

combo_section = soup.find_all("div", class_="combo-item")

combo_list = []
for item in combo_section:
    title = item.find("h2").text.strip()
    combo = item.find("code").text.strip()
    combo_list.append({
        "title": title,
        "combo": combo
    })

output = {
    "date": datetime.now().strftime("%Y-%m-%d"),
    "combos": combo_list
}

with open("public/data/daily_combos.json", "w", encoding='utf-8') as f:
    json.dump(output, f, indent=2, ensure_ascii=False)

print("✅ Combo data fetched and saved!")
