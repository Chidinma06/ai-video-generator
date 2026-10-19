import os
import requests
from dotenv import load_dotenv

load_dotenv()

PEXELS_API_KEY = os.getenv("PEXELS_API_KEY")

def fetch_images(keyword):
    os.makedirs("assets/images", exist_ok=True)
    headers = {"Authorization": PEXELS_API_KEY}
    url = f"https://api.pexels.com/v1/search?query={keyword}&per_page=5"
    response = requests.get(url, headers=headers)
    data = response.json()

    for i, photo in enumerate(data["photos"]):
        img_url = photo["src"]["medium"]
        img_data = requests.get(img_url).content
        with open(f"assets/images/image_{i}.jpg", "wb") as f:
            f.write(img_data)

    print("Images saved!")

