FROM python:3.9

ENV PYTHONUNBUFFERED=1

RUN mkdir /service
COPY protobufs/ /service/protobufs/
COPY register/ /service/register/
WORKDIR /service/register
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
RUN python -m grpc_tools.protoc -I ../protobufs --python_out=. --grpc_python_out=. ../protobufs/register.proto

EXPOSE 50051
ENTRYPOINT [ "python", "register.py" ]