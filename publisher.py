import os
from google.cloud import pubsub_v1

credentials_path = "private_key.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_path

publisher = pubsub_v1.PublisherClient()
topic_path = "projects/fifth-base-324714/topics/temperature-test"

data = "Merhaba dünya."
data = data.encode("utf-8")

future = publisher.publish(topic_path, data)
print(f'published message id {future.result()}')



