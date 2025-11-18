# Python Object Oriented Programming by Joe Marini course example
# Basic class definitions


# TODO: create a basic class
class Book:
  def __init__(self,title,author,pages,price):
      self.title = title
      self.author = author
      self.pages = pages
      self.price = price

# TODO: create instances of the class
book1=Book("Brave New World")
book2=Book("War and Peace")

# TODO: print the class and property
print(book1)
print(book1.title)