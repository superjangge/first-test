# This is a book
class book: 
  def __init__(self, name, category):
    self.name=name
    self.category=category

class mathbook(book):
  def __init__(self,name,subcategory):
      super().__init__(name,"terrorism")
      self.subcategory=subcategory

c=mathbook("Advanced Calculus", "Analysis") 
  


