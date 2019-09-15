from typing import List


class PersonWithOutStrAndEq():
    """PersonWithOutStrAndEq is the base class"""
    def __init__(self, first_name: str, last_name: str, id_number: str):
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.id_number: str = id_number


class StudentWithOutStrAndEq(PersonWithOutStrAndEq):
    """StudentWithOutStrAndEq is inhereted
       from the base class PersonWithOutStrAndEq"""
    def __init__(self, first_name: str, last_name: str,
                 id_number: str, scores: List):
        super().__init__(first_name, last_name, id_number)
        self.scores: List = scores
