from proto import transactions_pb2_grpc
import transactions_resources


class TransactionServiceServicer(transactions_pb2_grpc.TransactionServiceServicer):

    def GetTransaction(self, request, context):
        response = transactions_resources.read_transactions_database()
        return response
