#my_list = ['hello', 'world', 'python', 'programming']
#new_list = []

#for i, s in enumerate(my_list):
    #if i % 2 == 0:
        #new_list.append(s)
    #else:
        #new_list.append(s[::-1])

#print(new_list)

###########################################################

#my_list = ['Apple', 'appreciate', 'attractive', 'lame', 'are']
#new_list = []

#for letter in my_list:
    #if letter.startswith('a'):
        #new_list.append(letter)

    #elif letter.startswith('A'):
        #new_list.append(letter)

#print(new_list)

###########################################################

#my_list = ['Apple', 'appreciate', 'attractive', 'lame', 'are']
#new_list = []

#for letter in my_list:
    #if 'a' in letter.lower():
        #new_list.append(letter)

#print(new_list)

###########################################################

#firsts_users = \
    #[
        #{
            #'name': 'Sem',
            #'age': 11,
        #},

        #{
            #'name': 'Sasha',
            #'age': 21,
        #},

        #{
            #'name': 'David',
            #'age': 40,
        #},

        #{
            #'name': 'Yan',
            #'age': 19,
        #},

    #]

#youngest_age = float('inf')
#youngest_names = []
#longest_names = []
#max_length = 0
#total_age = 0
#num_users = len(firsts_users)


#for person in firsts_users:
    #age = person['age']
    #if age < youngest_age:
        #youngest_age = age
        #youngest_names = [person['name']]
    #elif age == youngest_age:
        #youngest_names.append(person['name'])

#print(youngest_names)

#for person in firsts_users:
    #name_length = len(person['name'])
    #if name_length > max_length:
        #longest_names = [person['name']]
        #max_length = name_length
    #elif name_length == max_length:
        #longest_names.append(person['name'])

#print(longest_names)

#for person in firsts_users:
    #total_age += person['age']

#average_age = total_age / num_users
#print("Средний возраст", average_age)  # я могу добавить int(average_age) тогда оно не будет во в флоте а нормальный возраст

###########################################################

#my_dict_1 = {
    #'brand': 'samsung',
    #'price': 2000,
#}
#my_dict_2 = {
    #'brand': 'motorola',
    #'price': 1300,
#}

#common_keys = list(my_dict_1.keys() & my_dict_2.keys())
#print(common_keys)

#my_dict_1['is_available'] = True
#my_dict_1['is_new']= False

#result = list(set(my_dict_1.keys()) - set(my_dict_1.keys() & my_dict_2.keys()))
#print(result)

#other_dict = {}

#for key in my_dict_1:
    #if key not in my_dict_2:
        #other_dict[key] = my_dict_1[key]

#print(other_dict)

#result_new_dict = {}

#for key in my_dict_1:
    #if key not in my_dict_2:
        #result_new_dict[key] = my_dict_1[key]
    #else:
        #result_new_dict[key] = [my_dict_1[key]], my_dict_2[key]

#for key in my_dict_2:
    #if key not in my_dict_1:
        #result_new_dict[key] = my_dict_2[key]

#print(result_new_dict)



















