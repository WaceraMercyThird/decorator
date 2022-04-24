# Decorators
def start_middle_end_decorator(func):

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print('Start')
        print('middle')
        print('End')
        return result
    return wrapper


@start_middle_end_decorator
def print_name():
    print('Alex')
  

print_name = start_middle_end_decorator(print_name)

# print_name()

@start_middle_end_decorator
def sum(x):
    return x + 5


result = sum(10)
print(result)
