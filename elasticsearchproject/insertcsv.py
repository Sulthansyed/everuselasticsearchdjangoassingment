from elasticsearch import helpers, Elasticsearch
import csv


es=Elasticsearch()



with open("/home/sulthan/Downloads/measurements.csv") as f:
	reader = csv.DictReader(f)
	helpers.bulk(es, reader, index='posts', doc_type='my_type')
