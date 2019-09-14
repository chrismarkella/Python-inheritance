import regular_inheritance   as ri
import dataclass_inheritance as di

poor_bob      = ri.StudentWithOutStrAndEq('Bob', 'Poor', '12', [10, 9, 9, 8, 10])
poor_bob_twin = ri.StudentWithOutStrAndEq('Bob', 'Poor', '12', [10, 9, 9, 8, 10])

# __str__ and __eq__ is not implemented "out of the box".
print(f'poor_bob:      {poor_bob}')
print(f'poor_bob_twin: {poor_bob_twin}')
print(f'poor_bob == poor_bob_twin: {poor_bob == poor_bob_twin}')
print(f'poor_bob is poor_bob_twin: {poor_bob is poor_bob_twin}')

print(f'After implementing the __str__ and the __eq__ functions.')
print(f'--------------------------------------------------------')

chris      = ri.Student('Christian', 'Markella', '123', [100, 99, 99, 98, 100])
chris_twin = ri.Student('Christian', 'Markella', '123', [100, 99, 99, 98, 100])
print(f'chris:-->     {chris}')
print(f'chris_twin--> {chris_twin}')
print(f'chris == chris_twin: {chris == chris_twin}')
print(f'chris is chris_twin: {chris is chris_twin}')

# ----------------Dataclass testing------------------------------------------
print(f'\n----------dataclass implementation----------------')
dataclass_bob      = di.Student('Bob', 'Dataclass', '12', [101, 99, 99, 98, 101])
dataclass_bob_twin = di.Student('Bob', 'Dataclass', '12', [101, 99, 99, 98, 101])

# "out of the box" __str__ and __eq__ ready to use.
print(f'dataclass_bob:      {dataclass_bob}')
print(f'dataclass_bob_twin: {dataclass_bob_twin}')
print(f'dataclass_bob == dataclass_bob_twin: {dataclass_bob == dataclass_bob_twin}')
print(f'dataclass_bob is dataclass_bob_twin: {dataclass_bob is dataclass_bob_twin}')

