class Searcher:
    """Модуль для пошуку предметів"""

    @staticmethod
    def by_name(items, name):
        name = name.lower()
        return [i for i in items if name in i.name.lower()]

    @staticmethod
    def by_id(items, id_):
        return [i for i in items if i.id == id_]
