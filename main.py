import random
import csv
from functools import wraps

def log(fn):
  """decorator that will print the name of function invoking
  and the arugments to that function"""
  @wraps(fn)
  def wrap_func(*args):
    func_sent = "Function: {}".format(fn.__name__)
    args_sent = "Arguments: {}".format(args)
    with open('deck.log', 'a') as file:
      file.write(func_sent)
      file.write("\n")
      file.write(args_sent)
      file.write("\n")
    return fn(*args)
  return wrap_func
  
class Deck:
  def __init__(self):
    self.cards = []
    self.create_cards_csv()
    self.removed_cards = []
    
  def create_cards(self):
    suits = ["Hearts","Diamonds","Clubs","Spades"]
    values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    self.cards = [Card(suit, value) for suit in suits for value in values]

  @log
  def create_cards_csv(self):
    with open('deck.csv', 'r') as csvfile:
      reader = csv.reader(csvfile, delimiter=",")
      rows = list(reader)
      self.cards = []
      #IF A DECK HASN'T BEEN SAVED - CREATE A NEW DECK
      if len(rows) < 1:
        self.create_cards()
      #OTHERWISE create the deck from the CSV file
      else:
        self.cards = [Card(row[1], row[0]) for row in rows]
  
  @log   
  def deal(self):
    removed_card = self.cards.pop()
    self.removed_cards.append(removed_card)
    return removed_card
  
  @log
  def shuffle(self):
    """shuffles the Deck class only if the deck is full"""
    if len(self.cards) == 52:
      random.shuffle(self.cards)
      return "Shuffled!"
    else:
      return "Error: Need a full deck to shuffle."
  
  @log
  def save(self):
    """this saves the Deck to a csv file"""
    with open('deck.csv', 'w') as csvfile:
      data_writer = csv.writer(csvfile, delimiter = ",")
      for x in self.cards:
        lst = [x.value, x.suite]
        data_writer.writerow(lst)

  def __iter__(self):
    """This makes the Deck class iterable"""
    return iter(self.cards)
  
  def __str__(self):
    str = 'Deck has these {} cards: '.format(len(self.cards))
    for i,x in enumerate(self.cards):
      str += x.__str__()
      if i < len(self.cards) - 1:
        str += "; "
    return str

class Card:
  def __init__(self, suit, value):
    self.suite = suit
    self.value = value
    
  def __str__(self):
    return "{} of {}".format(self.value, self.suite)

d = Deck()

# print(d.create_cards_csv())
print(d)
print(d.shuffle())
print(d)
print(d.save())
# print(d.deal())
# print(d)
# print(d.deal())

# print(d.deal())

# for card in d:
#   print(card)