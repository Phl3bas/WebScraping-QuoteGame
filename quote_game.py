from bs4 import BeautifulSoup
from requests import get
from csv import writer, DictReader
from random import randint

BASE_URL = "http://quotes.toscrape.com"


BASE_URL = "http://quotes.toscrape.com"
response = get(BASE_URL)
soup = BeautifulSoup(response.text, "html.parser")
quotes = soup.find_all(class_="quote")

with open("quote_data.csv","w") as f:
  csv_writer = writer(f)
  csv_writer.writerow(["id","author", "text", "link"])
  id_num = 1

  for quote in quotes:
    text = quote.find(class_="text").get_text()
    author = quote.find(class_="author").get_text()
    link = quote.find(class_="author").find_next_sibling()["href"]
    csv_writer.writerow([id_num,author, text.strip('\“').strip('\”'), link])
    id_num += 1

random_number = randint(1,id_num)

##TODO: Randomly pick line from csv, place author as namevariable and display quote, and input link into get_clue_data function to return the clues for that author.

with open("quote_data.csv") as f:
  csv_reader = DictReader(f)
  for i in csv_reader:
    if int(i["id"]) == random_number:
      ans = [int(i["id"]),i["author"],i["text"],i["link"]]
    
guess = 4
GAME_STATE = True

while(GAME_STATE):

  def get_clue_data(link):
    ABOUT_URL = BASE_URL + link
    about_req = get(ABOUT_URL)
    about = BeautifulSoup(about_req.text, "html.parser")
    return about

  if(guess == 4):
    print("Guess who said the following quote: ")
    print(ans[2])

  elif(guess == 3):
    clue = get_clue_data(ans[3])
    born = clue.find(class_="author-born-date").get_text()
    print("First clue: The author was born " + born)

  elif(guess == 2):
    clue = get_clue_data(ans[3])
    location = clue.find(class_="author-born-location").get_text()
    print("Second clue: Was Born " + location)

  elif(guess == 1):
    clue = get_clue_data(ans[3])
    first = clue.find(class_="author-title").get_text()[0]
    second = clue.find(class_="author-title").get_text().split(" ")[1][0]
    print("Last clue: Initials are " + first + second)

  else:
    print("Too bad, the answer was " + ans[1])
    GAME_STATE = False

  print("Clues Left: " + str(guess) + "/4" )
  user_ans = input()
  if user_ans.lower() == ans[1].lower():
    print(f"Yes! the answer was {ans[1]}")
  else:
    guess -= 1
