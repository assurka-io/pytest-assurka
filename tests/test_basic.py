# content of test_sample.py
def func(x):
    """ func description """
    return x + 1


def test_answer():
    """ some description """
    assert func(3) == 5


def another_test():
    """ some description """
    assert 1 == 1
