from Modules.magazine import Magazine
from Modules.book import Book
from Modules.cd import CD
from Modules.dvd import DVD


class Catalog:
    def __init__(self, catalog):
        self.catalog = catalog

    def search(self, input_search):
        list_result = []
        for catalog_item in self.catalog:
            for item in catalog_item:
                if input_search.lower() in item.title.lower():
                    if isinstance(item, Magazine):
                        list_result.append(f'Title : {item.title}, Volume : {item.volume}, Type Catalog : Magazine')
                    elif isinstance(item, Book):
                        list_result.append(f'Title : {item.title}, Volume : {item.dds_number}, Type Catalog : Magazine')
        return list_result