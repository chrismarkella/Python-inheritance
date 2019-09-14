from dataclasses import dataclass
from typing import List
@dataclass
class Person():
  """docstring for Person"""
  first_name: str
  last_name:  str
  id_number:  str

@dataclass
class Student(Person):
  scores: List
