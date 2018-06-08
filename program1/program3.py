"""reference https://stackoverflow.com/questions/50619742/read-csv-and-upload-data-to-elasticsearch"""
FILE_URL = "example.csv"
ES_HOST = {"host": "18.219.234.159", "port": 9200}
INDEX_NAME = 'tweettext'
TYPE_NAME = '_doc'
ID_FIELD = 'id'

import csv
from elasticsearch import Elasticsearch


csv_file_object = csv.reader(FILE_URL)
header = csv_file_object
header = [item for item in header]

# create ES client, create index
es = Elasticsearch(hosts=[ES_HOST])
if es.indices.exists(INDEX_NAME):
    res = es.indices.delete(index=INDEX_NAME)
request_body = {
    "settings": {
        "number_of_shards": 1,
        "number_of_replicas": 0
    }
}
res = es.indices.create(index=INDEX_NAME, body=request_body)


from elasticsearch import helpers, Elasticsearch
import csv

es = Elasticsearch()

with open('tweettext.csv') as f:
    reader = csv.DictReader(f)
    helpers.bulk(es, reader, index='tweettext', doc_type='_doc')
