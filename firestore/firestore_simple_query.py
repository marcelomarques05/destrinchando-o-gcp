import datetime
import threading
from time import sleep

from google.cloud import firestore

def get_simple_query():
    db = firestore.Client()
    # [START firestore_data_query]
    # Note: Use of CollectionRef stream() is prefered to get()
    docs = db.collection(u'pokemon').where(u'raro', u'==', True).stream()

    for doc in docs:
        print(f'{doc.id} => {doc.to_dict()}')
    # [END firestore_data_query]

get_simple_query()