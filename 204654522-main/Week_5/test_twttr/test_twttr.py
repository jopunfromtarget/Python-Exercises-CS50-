import pytest
from twttr import shorten

def main():
    test_twttr()

def test_twttr():
    assert shorten("Twitter") == "Twttr"
    assert shorten("tTtTtT") == "tTtTtT"
    assert shorten("TwItter, hello!?") == "Twttr, hll!?"
    assert shorten("123") == "123"
if __name__ == "__main__":
    main()
