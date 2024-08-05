import json
from typing import Generator

import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}


def get_suggestions(query) -> Generator[str, None, None]:
    url = f"https://suggestqueries.google.com/complete/search?client=firefox&q={query}"
    response = requests.get(url, headers=HEADERS)
    data = json.loads(response.text)
    for suggestion in data[1]:
        yield suggestion

