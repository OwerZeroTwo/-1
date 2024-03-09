def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(a=2)
print_params(b='Что-то')
print_params(c=False)
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [5, 'бестия', False]

values_dict = {'a': 20, 'b': 'Дурка', 'c': True}

print_params(*values_list)

print_params(**values_dict)

values_list_2 = [48, 'Ничего']

print_params(*values_list_2, 42)
