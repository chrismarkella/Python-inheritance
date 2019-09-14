class Person():
  """Person is the base class"""
  def __init__(self, first_name, last_name, id_number):
    self.first_name = first_name
    self.last_name = last_name
    self.id_number = id_number
  def __str__(self):
    return (
      f'first name: {self.first_name}\n'
      f'last name: {self.last_name}\n'
      f'id number: {self.id_number}'
           )

class Student(Person):
  """Student is inhereted from the base class Person"""
  def __init__(self, first_name, last_name, id_number, scores):
    super().__init__(first_name, last_name, id_number)
    self.scores = scores

  def __str__(self):
    return (
      f'{super().__str__()}\n'
      f'scores: {self.scores}'
      )

chris = Student('Chris', 'Markella', '123', [100, 99, 98, 100])
print(chris)
    