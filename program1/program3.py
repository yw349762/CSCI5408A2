import csv
import json

from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
  print(es)



def csv_reader(file_obj, delimiter=','):
   reader = csv.reader(file_obj)
   i = 1
   results = []
   for row in reader:
     print(row)
     es.index(index='product', doc_type='prod', id=i, body=json.dump([row for row in reader], file_obj))
     i = i + 1
     results.append(row)
     print(row)


 if __name__ == "__main__":
  with open("tweettext.csv") as f_obj:
     csv_reader(f_obj)s.bulk(es, reader, index='tweettext', doc_type='my-type')