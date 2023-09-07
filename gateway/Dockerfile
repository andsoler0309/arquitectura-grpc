FROM python:3.9

ENV PYTHONUNBUFFERED=1

RUN mkdir /service
COPY protobufs/ /service/protobufs/
COPY gateway/ /service/gateway/
WORKDIR /service/gateway
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
RUN python -m grpc_tools.protoc -I ../protobufs --python_out=. \
           --grpc_python_out=. ../protobufs/register.proto

EXPOSE 5000
ENV FLASK_APP=gateway.py
ENTRYPOINT [ "flask", "run", "--host=0.0.0.0"]
