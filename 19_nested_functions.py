def calculate_result(a, b):

    def add_numbers():
        return a+b
    
    def divide_numbers(value):
        return value / b
    
    def multiply_numbers(value):
        return value * b
    
    result = add_numbers()
    result = divide_numbers(result)
    result = multiply_numbers(result)

    return result



final_result = calculate_result(10, 20)
print(final_result)