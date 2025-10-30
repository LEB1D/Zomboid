import csv
import json
import xml.etree.ElementTree as ET
import os


class CsvReader:
    def __init__(self, path):
        self.path = path

    def read(self):
        with open(self.path, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            data = []
            for row in reader:
                # Перетворюємо ключі в нижній регістр
                data.append({k.lower(): v for k, v in row.items()})
            return data


class JsonReader:
    def __init__(self, path):
        self.path = path

    def read(self):
        with open(self.path, encoding="utf-8") as f:
            data = json.load(f)
            # Якщо ключі великі — теж у нижній регістр
            return [{k.lower(): v for k, v in item.items()} for item in data]


class XmlReader:
    def __init__(self, path):
        self.path = path

    def read(self):
        tree = ET.parse(self.path)
        root = tree.getroot()
        data = []
        for item in root.findall("item"):
            row = {child.tag.lower(): child.text for child in item}
            data.append(row)
        return data


def get_reader(path):
    ext = os.path.splitext(path)[1].lower()
    if ext == ".csv":
        return CsvReader(path)
    elif ext == ".json":
        return JsonReader(path)
    elif ext == ".xml":
        return XmlReader(path)
    else:
        raise ValueError(f"Unsupported file format: {ext}")
