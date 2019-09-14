from typing import List

class Person():
  """Person is the base class"""
  def __init__(self, first_name: str, last_name: str, id_number: str):
    self.first_name: str = first_name
    self.last_name: str = last_name
    self.id_number: str = id_number
  def __str__(self):
    return (
      f'first name: {self.first_name}, '
      f'last name: {self.last_name}, '
      f'id number: {self.id_number}, '
           )
  def __eq__(self, other):
    return (
      self.first_name == other.first_name and
      self.last_name  == other.last_name  and
      self.id_number  == other.id_number
           )

class Student(Person):
  """Student is inhereted from the base class Person"""
  def __init__(self, first_name: str, last_name: str, id_number: str, scores: List):
    super().__init__(first_name, last_name, id_number)
    self.scores: List = scores

  def __str__(self):
    return (
      f'{super().__str__()}, '
      f'scores: {self.scores}'
           )
  def __eq__(self, other):
    return (
      super().__eq__(other) and
      self.scores == other.scores
           )
