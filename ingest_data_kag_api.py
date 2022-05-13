import time
import csv
import kaggle
import json
import os
import requests as rq
from google.cloud import pubsub_v1
from csv import reader

project_id = "gcp-project-346311"
topic_name = "my_pub_topic1"
api_key = "d3a9b381b061bb64b93dc2228528df1c"
publisher = pubsub_v1.PublisherClient(batch_settings=pubsub_v1.types.BatchSettings(max_latency=5))
topic_path = publisher.topic_path(project_id, topic_name)
dir = os.getcwd()
kaggle.api.authenticate()
kaggle.api.dataset_download_files('gennadiyr/us-equities-news-data', path=dir, unzip=True)
data_file = os.path.join(dir,'us_equities_news_dataset.csv')
f_data = open(data_file)
jsonfile = open('file.json', 'w')
n=1
flag=0
fieldnames=("id","ticker","title","category","content","release_date","provider","url","article_id")
reader = csv.DictReader( f_data, fieldnames)

for row in reader:
#for line in f_data:
   # time.sleep(2)
    if(n==10000):
           break
    else:
           if flag==0:
                flag=1
                pass
           else:
            #  data=json.dumps(row.encode(utf-8))
              data = json.dumps(row).encode('utf-8')
              publisher.publish(topic_path, data=data)
              n=n+1
#            print("Pushed message to topic.")
              #data=line.encode('utf-8')
   #           print(data)

print("Published messages with batch settings to {}.".format(topic_path))
