import pytest

"""
-------------------------
-- Basic fixtures demo --
-------------------------
"""
@pytest.fixture
def hello_world():
  return "hello, world!"

def test_string1(hello_world):
  str1 = "hello, world!"
  assert str1 == hello_world

def test_string2(hello_world):
  str2 = "HELLO, WORLD!"
  assert str2.lower() == hello_world

def test_string3_skip(hello_world):
  str3 = "Hello world!"
  pytest.skip(f'Skipping, since test is intentionally wrong')
  assert str3 == hello_world

def test_string3_throws(hello_world):
  #str3 = "hello, world!"
  str3 = "Hello world!"
  with pytest.raises(AssertionError) as e_info:
    assert str3 == hello_world

"""
-------------------------
-- Input fixtures demo --
-------------------------
"""
@pytest.fixture
def strings():
  return {
    1: "Hello, world!"
  }

def test_input_string1(strings):
  str1 = "Hello, world!"
  assert str1 == strings[1]
