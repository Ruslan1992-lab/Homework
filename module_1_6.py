my_dict = {'Ruslan': 1992, 'Elina': 1987, 'Evgeniy': 1993}
print(my_dict)
print(my_dict.get('Ruslan'))
print(my_dict.get('Vladimir'))
my_dict.update({'Luciay': 1991 ,'German': 1996})
del my_dict['Evgeniy']
print(my_dict)


my_set = {1, 1, 1, 2, 2, 'Pacha', 'Pacha', True, True}
print(set(my_set))
print(my_set.add('Kino'))
print(my_set.add('Boock'))
print(my_set.discard(True))
print(my_set)