def test_function(arks):
    n = arks
    def inner_function(n):
        print("Я в области видимости функции test_function")
    inner_function(5)
print(test_function(0))
print(inner_function(6))