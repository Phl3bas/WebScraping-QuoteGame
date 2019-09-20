from bs4 import BeautifulSoup
from requests import get


def get_quotes(BASE_URL,URL=None):
  QUOTES = []
  response = get(URL or BASE_URL)
  soup = BeautifulSoup(response.text, "html.parser")
  quotes = soup.find_all(class_="quote")

  next_btn = soup.find(class_="next")
  next_link = next_btn.find("a")["href"] if next_btn else None
  NEXT_URL = BASE_URL + next_link if next_btn else None

  for quote in quotes:
    text = quote.find(class_="text").get_text()
    author = quote.find(class_="author").get_text()
    link = quote.find(class_="author").find_next_sibling()["href"]
    QUOTES.append({'author':author,'text':text,'link':link})


  if next_btn:
    get_quotes(BASE_URL,NEXT_URL)

  return QUOTES
