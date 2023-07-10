import pytest
from src.phone import Phone

@pytest.fixture
def my_phone():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_phone_init(my_phone):
    assert my_phone.name == "iPhone 14"
    assert my_phone.price == 120_000
    assert my_phone.quantity == 5
    assert my_phone.number_of_sim == 2


