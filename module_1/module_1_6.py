# Словарь my_dict
my_dict = {
    "Company":"Sprut",
    "model":"SMP",
    "year": 2022
    }
print(my_dict)
print("Company Name: ", my_dict["Company"])
print(my_dict.get('color'))
my_dict["fruit_1"] =  'apples'
my_dict["fruit_2"] = 'mango'
del my_dict["year"]
print("Modifid my_dict: ", my_dict)

# множество my_set
my_set = {1,1,2,2,2,3,5,6,11,15,(1,2,3),'String1', 'String1', 2,5,5,11,15}
print(my_set)
my_set.add(17)
my_set.add(19)
my_set.discard(((1,2,3)))
print("Modifid my_set: ", my_set)
