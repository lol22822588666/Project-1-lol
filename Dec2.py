# Декоратор для измерения времени выполнения функции
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Время выполнения функции {func.__name__}: {end_time - start_time}")
        return result
    return wrapper

# Декоратор для логирования вызовов функции
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Вызов функции {func.__name__} с аргументами {args}, {kwargs}")
        result = func(*args, **kwargs)
        return result
    return wrapper

@logger
@timer
def my_function(x, y):
    time.sleep(2)
    return x + y

my_function(3, 5)