from concurrent import futures
import time
import grpc
import register_pb2_grpc
import register_pb2
import random


class RegisterService(register_pb2_grpc.RegisterServiceServicer):
    def Register(self, request, context):
        # generate a random number between 0 and 100, this should be 80% greater than 10
        if random.randint(0, 100) > 10:
            return register_pb2.RegisterResponse(code=200, message="success")

        return register_pb2.RegisterResponse(code=500, message="error")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    register_pb2_grpc.add_RegisterServiceServicer_to_server(RegisterService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("register server started")
    server.wait_for_termination()
    # try:
    #     while True:
    #         time.sleep(60 * 60 * 24)
    # except KeyboardInterrupt:
    #     server.stop(0) 


if __name__ == '__main__':
    serve()