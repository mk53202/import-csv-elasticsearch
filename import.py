# https://elasticsearch-py.readthedocs.io/en/master/
# https://stackoverflow.com/questions/44696039/python-elasticsearch-bulk-index-datatype
# https://stackoverflow.com/questions/41573616/index-csv-to-elasticsearch-in-python
# http://10.0.1.215:9200/_cat/indices?v
# http://10.0.1.215:9200/_search
# http://10.0.1.215:9200/_search?q=65.6

from elasticsearch import helpers, Elasticsearch
import csv

# es = Elasticsearch()

es = Elasticsearch('10.0.1.215:9200')
es_info = es.info()

# es = Elasticsearch(
#     ['10.0.1.215'],
#     http_auth=('user', 'secret'),
#     scheme="https",
#     port=9200,
# )

index_name = 'temperature_data'

with open('/tmp/temperature.csv') as f:
    reader = csv.DictReader(f)
    helpers.bulk(es, reader, index=index_name, doc_type='my-type')
