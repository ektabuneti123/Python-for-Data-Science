import requests
from bs4 import BeautifulSoup

url = "https://www.wikipedia.org/"
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})

soup = BeautifulSoup(response.text, "html.parser")

print("First 3 Paragraphs:")
for paragraph in soup.find_all("p")[:3]:
    print(paragraph.get_text(strip=True))

print("\nImage URLs:")
for image in soup.find_all("img"):
    print(image.get("src"))

links = soup.find_all("a", href=True)
print("\nTotal Number of Links:", len(links))

print("\nHeadings:")
for heading in soup.find_all(["h1", "h2", "h3"]):
    print(heading.get_text(strip=True))

print("\nLanguage Names:")
for language in soup.select(".central-featured-lang"):
    print(language.get_text(" ", strip=True))
