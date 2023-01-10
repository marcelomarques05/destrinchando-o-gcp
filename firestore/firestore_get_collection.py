import datetime
import threading
from time import sleep

from google.cloud import firestore

def quickstart_get_collection():
    db = firestore.Client()
    # [START firestore_setup_dataset_read]
    # [START quickstart_get_collection]
    users_ref = db.collection(u'pokemon')
    docs = users_ref.stream()

    for doc in docs:
        print(f'{doc.id} => {doc.to_dict()}')
    # [END quickstart_get_collection]
    # [END firestore_setup_dataset_read]

quickstart_get_collection()