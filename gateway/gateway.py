import os
from flask import Flask, request
from config import register_channel
from register_pb2 import RegisterRequest
from register_pb2_grpc import RegisterServiceStub
from monitor import monitor_registration_errors

app = Flask(__name__)

register_client = RegisterServiceStub(register_channel)

@app.route("/register", methods=["POST", "GET"])
@monitor_registration_errors
def register():
    register_request = RegisterRequest(
        id=1,
        name='test'
    )

    register_response = register_client.Register(register_request)
    output = f"El registro fue exitoso"
    if register_response.code != 200:
        output = "Estamos teniendo problemas intenta mas tarde"

    return output, register_response

