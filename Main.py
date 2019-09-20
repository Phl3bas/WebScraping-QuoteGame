from app.Config import BASE_URL
from app.Game import start_game
from app.Scraper import get_quotes

if __name__ == "__main__":
  QUOTES = get_quotes(BASE_URL)
  start_game(QUOTES)



