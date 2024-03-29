import time


def speed_calc_decorator(function):
    def wrapper_function():
        start_time = time.time()
        function()
        end_time = time.time()
        print(f"{function.__name__} runs {end_time - start_time} seconds")
        return end_time - start_time
    return wrapper_function


@speed_calc_decorator
def fast_function():
    for _ in range(10000000):
        pass


@speed_calc_decorator
def slow_function():
    for _ in range(100000000):
        pass


def main():
    first_run = fast_function()
    second_run = slow_function()
    print(f"First run: {first_run}, Second run: {second_run}")
    return second_run - first_run


def logging_decorator(fn):
    def wrapper(*args, **kwargs):
        print(f"You called {fn.__name__}{args}")
        result = fn(args[0], args[1], args[2])
        print(f"It returned: {result}")

    return wrapper


@logging_decorator
def a_function(a, b, c):
    return a * b * c


a_function(1, 2, 3)

if __name__ == "__main__":
    main()