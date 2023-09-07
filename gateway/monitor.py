from register_pb2 import RegisterRequest
from register_pb2_grpc import RegisterServiceStub
from config import register_channel
from functools import wraps

register_client = RegisterServiceStub(register_channel)

def monitor_registration_errors(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Call the wrapped function
        message, response = func(*args, **kwargs)

        # Log errors if the response code is not 200
        if response.code != 200:
            with open('error.log', 'a') as f:
                f.write(f'Error: {response.message}\n')

        return message, response.code

    return wrapper
