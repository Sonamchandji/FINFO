import time
import csv
import kaggle
import json
import os
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
dir=os.getcwd()
kaggle.api.dataset_download_files('gennadiyr/us-equities-news-data',path=dir,unzip=True)
local_path=os.path.join(dir,'us_equities_news_dataset.csv')
file_name=' us_equities_news_dataset.csv'
credential_path ="gcp-project-346311-7d11c0803e0c.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path
bucket_name='gs://finfo-2022/temp'
os.system('gsutil cp '+ file_name +' '+ bucket_name)
