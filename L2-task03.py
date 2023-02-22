my_int = 5
my_str = "Hello"
my_float = 1.2
my_bool = True
my_dict = {'city': 'Minsk', 'country': 'Belarus'}

super_list = [my_int, my_float, my_str, my_bool, my_dict]
for i in super_list:
    print(f'{i} тип {type(i)}')