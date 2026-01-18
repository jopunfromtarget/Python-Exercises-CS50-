import pytest
from bank import value

def main():
    test_bank()

def test_bank():

    assert value("hello") == 0
    assert value("HELLO?") == 0
    assert value("hey there pretty thang!") == 20
    assert value("Welcome to my dungeon") == 100

if __name__ == "__main__":
    main()
