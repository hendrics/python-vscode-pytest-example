
from mymodule import me

def test_myself_my_name():
    assert me.myself("Vader") == "Hello, Vader"

def test_myself_my_name2():
    assert me.myself("Luke") == "Hello, Luke"

def test_raise_something():
    me.raise_something()
