from random import choice
from bs4 import BeautifulSoup
from requests import get
import Scraper

BASE_URL = "http://quotes.toscrape.com"
QUOTES = Scraper.get_quotes(BASE_URL)
ans = choice(QUOTES)
guess = 4

GAME_STATE = True

while(GAME_STATE):

  def get_clue_data(link):
    ABOUT_URL = BASE_URL + link
    about_req = get(ABOUT_URL)
    about = BeautifulSoup(about_req.text, "html.parser")
    return about

  def end_game(user_input):
    global guess
    global GAME_STATE
    
    if user_input.lower() == "y":
      BASE_URL = "http://quotes.toscrape.com"
      QUOTES = Scraper.get_quotes(BASE_URL)
      guess = 4
      ans = choice(QUOTES)
      return ans
    else:
      GAME_STATE = False

  print("")
  if(guess == 4):
    print("Guess who said the following quote: ")
    print(ans["text"])

  elif(guess == 3):
    clue = get_clue_data(ans["link"])
    born = clue.find(class_="author-born-date").get_text()
    print("First clue: The author was born " + born)

  elif(guess == 2):
    clue = get_clue_data(ans["link"])
    location = clue.find(class_="author-born-location").get_text()
    print("Second clue: Was Born " + location)

  elif(guess == 1):
    clue = get_clue_data(ans["link"])
    first = clue.find(class_="author-title").get_text()[0]
    second = clue.find(class_="author-title").get_text().split(" ")[1][0]
    print("Last clue: Initials are " + first + second)

  else:
    print("Too bad, the answer was " + ans["author"])
    ans = end_game(input("Want to go again? y/n "))
    continue

  print("Clues Left: " + str(guess) + "/4" )
  user_ans = input()
  if user_ans.lower() == ans["author"].lower():
    print(f"Yes! the answer was {ans['author']}")
    ans = end_game(input("Want to go again? y/n "))
  else:
    guess -= 1





