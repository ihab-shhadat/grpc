import json
from google.protobuf.json_format import Parse
from proto.transactions_pb2 import Transaction


def read_transactions_database():
    transactions = open("data/transaction.json", 'r')
    data = json.load(transactions)
    return Parse(json.dumps(data), Transaction())
