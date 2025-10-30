import pytest
from Zomboid.models import Item
from Zomboid.inventory import Inventory
from Zomboid.file_readers import CsvReader, JsonReader, XmlReader


# ======== ТЕСТИ ДЛЯ Item ========


def test_item_init_types():
    item = Item("1", "Hammer", "Tool", "New", "5")
    assert item.id == 1
    assert item.amount == 5
    assert item.name == "Hammer"


def test_item_repr():
    item = Item(2, "Nails", "Hardware", "Used", 10)
    assert "Nails" in repr(item)
    assert "Used" in repr(item)


# ======== ТЕСТИ ДЛЯ Inventory ========

@pytest.fixture
def sample_inventory(tmp_path):
    csv_path = tmp_path / "items.csv"
    csv_path.write_text(
        "id,name,type,condition,amount\n"
        "1,Hammer,Tool,New,5\n"
        "2,Nails,Hardware,Used,10\n"
        "3,Screwdriver,Tool,New,3\n",
        encoding="utf-8"
    )
    return Inventory(csv_path)


def test_search_by_name(sample_inventory):
    results = sample_inventory.search_by_name("Nails")
    assert len(results) == 1
    assert results[0].name == "Nails"


def test_get_by_id(sample_inventory):
    results = sample_inventory.get_by_id(3)
    assert len(results) == 1
    assert results[0].name == "Screwdriver"


def test_state_percentages(sample_inventory):
    result = sample_inventory.state_percentages()
    # New = 8 шт., Used = 10 шт.
    assert round(result["New"], 2) == pytest.approx(44.44, 0.1)
    assert round(result["Used"], 2) == pytest.approx(55.56, 0.1)


# ======== ТЕСТИ ДЛЯ FILE READERS ========

def test_csv_reader(tmp_path):
    file = tmp_path / "data.csv"
    file.write_text(
        "id,name,type,condition,amount\n1,Hammer,Tool,New,5\n", encoding="utf-8")
    reader = CsvReader(file)
    data = reader.read()
    assert data[0]["name"] == "Hammer"


def test_json_reader(tmp_path):
    file = tmp_path / "data.json"
    file.write_text(
        '[{"id": 1, "name": "Hammer", "type": "Tool", "condition": "New", "amount": 5}]', encoding="utf-8")
    reader = JsonReader(file)
    data = reader.read()
    assert data[0]["id"] == 1


def test_xml_reader(tmp_path):
    file = tmp_path / "data.xml"
    file.write_text(
        "<items><item><id>1</id><name>Hammer</name><type>Tool</type><condition>New</condition><amount>5</amount></item></items>",
        encoding="utf-8"
    )
    reader = XmlReader(file)
    data = reader.read()
    assert data[0]["name"] == "Hammer"
