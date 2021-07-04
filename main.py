import grpc
from concurrent import futures
import time
from proto import transactions_pb2_grpc
from server.transactions_server import TransactionServiceServicer

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
transactions_pb2_grpc.add_TransactionServiceServicer_to_server(TransactionServiceServicer(), server)
server.add_insecure_port('[::]:50051')
server.start()
print('Server Ready. Listening on port 50051.')

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
