import datetime
import pytest
import time

print(datetime.datetime.now())

def test_func(benchmark):
    benchmark(time.sleep, 1)

# @pytest.fixture
# def init_list():
#     return []

# # Declare the fixture with autouse
# @pytest.fixture(autouse=True)
# def add_numbers_to_list(init_list):
#     init_list.extend([i for i in range(10)])

# # Complete the tests
# def test_elements(init_list):
#     assert (1 in init_list())
#     assert (9 in init_list())


# def division(a, b):
#     return a/b

# def squared(number):
#     return number * number

# def test_squared():
#     assert squared(-2) == squared(2)

# with open("hello_world", "w") as hello_file:
#     hello_file.write("Hello world \n")

# @pytest.mark.skip
# def test_raises():
#     with pytest.raises(ZeroDivisionError):
#         division(a=25, b=0)

# def get_length(string):
#     return len(string)

# @pytest.mark.skipif('2 * 2 == 5')
# def test_get_len():
#     assert get_length('123') == 3

# @pytest.mark.xfail
# def test_square_two():
#     assert squared('a')

# @pytest.fixture
# def data():
#     return [0, 1, 1, 2, 3, 5, 8, 9, 10]

# def test_list(data):
#     assert len(data) == 9

 