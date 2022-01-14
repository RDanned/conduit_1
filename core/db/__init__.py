from pymongo import MongoClient
from pymongo.collection import Collection
from core.settings import settings
from . import users

client = MongoClient(settings.mongo_url)
db = client['conduit_1']

instances: dict[str, Collection] = dict()
instances[users.COLLECTION_NAME] = db[users.COLLECTION_NAME]


def get_instance(collection_name: str):
    return instances[collection_name]


users = get_instance('users')
