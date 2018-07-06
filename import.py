from elasticsearch import helpers, Elasticsearch
import csv

es = Elasticsearch()

with open('/tmp/temperature.csv') as f:
    reader = csv.DictReader(f)
    helpers.bulk(es, reader, index='my-index', doc_type='my-type')
    # for line in reader:
        # print line
