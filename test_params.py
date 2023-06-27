import pytest

"""
-----------------------------
-- Basic parameterize demo --
-----------------------------
"""

@pytest.fixture
def shell_to_cart_elem():
  return {
    "s": 1,
    "p": 3,
    "d": 6,
    "f": 10,
  }

# 3 tests total
@pytest.mark.parametrize("shell1", ["s", "p", "d"])
def test_shell_am(shell1, shell_to_cart_elem):
   assert shell_to_cart_elem[shell1] <= 6 

# 12 tests total
@pytest.mark.parametrize("shell1", ["s", "p", "d", "f"])
@pytest.mark.parametrize("shell2", ["s", "p", "d"])
def test_shell_pair_am(shell1, shell2, shell_to_cart_elem):
  assert shell_to_cart_elem[shell1] * shell_to_cart_elem[shell2] <= 60
