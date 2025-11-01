import sys
import requests
from bs4 import BeautifulSoup

def main():
    if len(sys.argv) != 2:
        print("not enough arguments")
        return

    word = sys.argv[1].lower()
    url = f"https://www.oxfordlearnersdictionaries.com/definition/english/{word}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"error: {e}")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    definitions = [d.text.strip() for d in soup.find_all("span", class_="def")]

    if not definitions:
        print(f"no definition found for '{word}'.")
        return

    print(definitions[0])

if __name__ == "__main__":
    main()
