from random import choice
from bs4 import BeautifulSoup
from requests import get
from app.config import BASE_URL

def start_game(QUOTES):
  user_ans = ""
  guesses = 4
  ans = choice(QUOTES)

  def get_clue_data(link):
      ABOUT_URL = BASE_URL + link
      about_req = get(ABOUT_URL)
      about = BeautifulSoup(about_req.text, "html.parser")
      return about
    
  print("")
  print("Guess who said the following quote: ")
  print(ans["text"])

  while user_ans != ans["author"] and guesses != 0:
    print("Clues Left: " + str(guesses) + "/4" )
    user_ans = input()
    guesses -= 1
    print("")

    if(user_ans.lower() == ans["author"].lower()):
      print("THATS CORRECT!")
      break
      
    elif(guesses == 3):
      clue = get_clue_data(ans["link"])
      born = clue.find(class_="author-born-date").get_text()
      print("First clue: The author was born " + born)

    elif(guesses == 2):
      clue = get_clue_data(ans["link"])
      location = clue.find(class_="author-born-location").get_text()
      print("Second clue: Was Born " + location)

    elif(guesses == 1):
      clue = get_clue_data(ans["link"])
      first = clue.find(class_="author-title").get_text()[0]
      second = clue.find(class_="author-title").get_text().split(" ")[1][0]
      print("Last clue: Initials are " + first + second)

    else:
      print("Too bad, the answer was " + ans["author"])
      break

  again = ""
  while again.lower() not in ("y", "yes", "n", "no"):
    again = input("Would you like to play again? (y/n): ")
    if again.lower() in ("y", "yes"):
      return start_game(QUOTES)
    else:
      print("Sorry i didnt get that?")
      print("")
  
  print("Thanks for playing!")
