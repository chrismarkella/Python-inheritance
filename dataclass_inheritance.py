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
  scores: List[int]

bob = Person('Bob', 'Dilan', '123')
print(bob)

chris      = Student('Christian', 'Markella', '1234', [100, 99, 99, 98, 100])
chris_twin = Student('Christian', 'Markella', '1234', [100, 99, 99, 98, 100])
print(chris)
print(chris_twin)
print(f'chris == chris_twin: {chris == chris_twin}')
print(f'chris is chris_twin: {chris is chris_twin}')