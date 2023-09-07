import os
from flask import Flask, request
import grpc

from register_pb2 import RegisterRequest
from register_pb2_grpc import RegisterServiceStub

app = Flask(__name__)

register_host = os.getenv("REGISTER_HOST", "localhost")
register_port = os.getenv("REGISTER_PORT", "50051")
register_channel = grpc.insecure_channel(f"{register_host}:{register_port}")

register_client = RegisterServiceStub(register_channel)


@app.route("/register", methods=["POST", "GET"])
def register():
    register_request = RegisterRequest(
        id=1,
        name='test'
    )

    register_response = register_client.Register(register_request)
    print(register_response)

    output = f"El registro fue exitoso"
    if register_response.code != 200:
        output = "Estamos teniendo problemas intenta mas tarde"

    return output, register_response.code

