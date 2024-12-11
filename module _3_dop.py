def calculate_structure_sum(args):
    sum = 0
    for elem in args:
        if isinstance(elem, (int, float, bool)):
            sum += elem
        if isinstance(elem, str):
            sum += len(elem)
        if isinstance(elem, (list, tuple, set)):
            sum += calculate_structure_sum(elem)
        if isinstance(elem, dict):
            sum += calculate_structure_sum(elem.items())
    return sum



data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)

print(result)