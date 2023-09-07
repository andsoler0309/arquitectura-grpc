import os
import grpc

register_host = os.getenv("REGISTER_HOST", "localhost")
register_port = os.getenv("REGISTER_PORT", "50051")
register_channel = grpc.insecure_channel(f"{register_host}:{register_port}")
