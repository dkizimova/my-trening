def print_params(a=1, b='string', c=True):
    print(a, b, c)

print_params()
print_params(a=2, b='hello')
print_params(a=8, c=False)
print_params(b=25)
print_params(c=[1, 2, 3])


values_list=[3, 'bye', True]
values_dict={'a': 'python', 'b': True, 'c':7 }

print_params(*values_list)
print_params(**values_dict)

values_list_2=[54.32, 'string']

print_params(*values_list_2, 42)