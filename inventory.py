from Zomboid.models import Item
from file_readers import get_reader
from collections import Counter


class Inventory:
    def __init__(self, path):
        reader = get_reader(path)
        self.items = [Item(**data) for data in reader.read()]

    def show_page(self, page, page_size=10):
        start = (page - 1) * page_size
        end = start + page_size
        for item in self.items[start:end]:
            print(item)

    def get_by_id(self, id_):
        return [i for i in self.items if i.id == id_]

    def search_by_name(self, name):
        name = name.lower()
        return [i for i in self.items if name in i.name.lower()]

    def state_percentages(self, name_filter=None):
        filtered = self.items
        if name_filter:
            filtered = [i for i in self.items if name_filter.lower()
                        in i.name.lower()]
        total = sum(i.amount for i in filtered)
        if total == 0:
            return {}
        counter = Counter()
        for i in filtered:
            counter[i.condition] += i.amount
        return {cond: round(amt / total * 100, 2) for cond, amt in counter.items()}
