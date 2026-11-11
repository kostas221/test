import pytest
# Φέρνουμε μέσα τις κλάσεις που γράψαμε στο inventory.py
from inventory import Item, OutOfStockError, ItemNotFoundError, Inventory

@pytest.fixture
def sample_item():
    return Item(name="Laptop", stock=10, price=1000.0)

def test_remove_stock(sample_item):
    sample_item.remove_stock(3)
    assert sample_item._stock == 7

# ... εδώ θα γράψεις τα επόμενα tests σου ...