import time
import csv
import kaggle
import json
import requests as rq
from google.cloud import pubsub_v1
from csv import reader
from google.cloud import storage

project_id = "gcp-project-346311"
topic_name = "my_pub_topic1"
api_key = "d3a9b381b061bb64b93dc2228528df1c"
publisher = pubsub_v1.PublisherClient(batch_settings=pubsub_v1.types.BatchSettings(max_latency=5))
topic_path = publisher.topic_path(project_id, topic_name)
kaggle.api.authenticate()
kaggle.api.dataset_download_files('gennadiyr/us-equities-news-data', path='/home/itproject2022bootcamp', unzip=True)
local_data = '/home/itproject2022bootcamp/ us_equities_news_dataset.csv'
file_name=' us_equities_news_dataset.csv'
upload(bucket_name,local_data,file_name)

storage_client=storage.Client(project='gcp-project-346311')
def create_bucket(dataset_name):
     # creating a new bucket
     bucket = storage_client.create_bucket(dataset_name)
     print('buckey created'.format(bucket.name))


def upload_blob(bucket_name,source_file_name,destination_blob_name):
# uploads the file to the bucket
     bucket=storage_client.get_bucket(bucket_name)
     blob=bucket.blob(destination_blob_name)
     blob.upload_from_filename(source_file_name)
     print('file uploaded to',destination_blob_name)


bucket_name = ' FINFO_publc_data'
try:
    create_bucket(bucket_name)
except:
    pass

upload_blob(bucket_name,local_data,file_name)
print('Data inside of', bucket_name,':')
list_blobs(bucket_name)
