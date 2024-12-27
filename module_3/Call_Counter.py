calls = 0

def count_calls():
    global calls
    calls += 1
    return calls

def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())

def is_contains(string, list_to_search):
    count_calls()
    cop_string = string.lower()
    cop_list_to_search = []
    for elem in list_to_search:
        cop_list_to_search.append(elem.lower())
        result = any(item in cop_string for item in cop_list_to_search)
    return result
    print(cop_string, cop_list_to_search)

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)

#(8, 'CAPYBARA', 'capybara')
#(10, 'ARMAGEDDON', 'armageddon')
#True
#False
#4
