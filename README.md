# arquitectura-disponibilidad-grpc


### steps to run the project

1. Install docker and docker-compose
2. Run the following command to build the project
```
docker-compose build
```
3. Run the following command to run the project
```
docker-compose up
```

4. in a new terminal run the following command to run the client
```
python front/front.py
```

5. get the total error logs of the server
```
docker-compose exec gateway sh
wc -l error.log
```

5.1 if you want to see the error logs of the server
```
cat error.log
```

