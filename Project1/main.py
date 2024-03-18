import json
from Modules.magazine import Magazine
from Modules.book import Book
from Modules.catalog import Catalog


f = open('catalog/catalog.json')
data_json = json.load(f)

books = []
magazines = []

for item in data_json:
    if item['source'] == 'book':
        books.append(
            Book(
                title=item['title'],
                subject=item['subject'],
                upc=item['upc'],
                isbn=item['issbn'],
                authors=item['authors'],
                dds_number=item['dds_number']
            )
        )
    elif item['source'] == 'magazine':
        magazines.append(
            Magazine(
                title=item['title'],
                subject=item['subject'],
                upc=item['upc'],
                volume=item['volume'],
                issue=item['issue']
            )
        )

catalog_all = [books, magazines]
input_search = 'test'
result = Catalog(catalog_all).search(input_search)

for index, result in enumerate(result):
    print(f'result ke-{index+1} | {result}')
