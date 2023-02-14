# upload_service

## Description
Upload Service is responsible for Uploading Video to the GridFS(MongoDB). After the successful upload, 
the uploaded video id (fid) will be sent to the RabbitMQ Queue that then will be consumed by the 
`converter_service`.

# How to run the application?
1. You have the Mongodb service running on your machine. If not, please make sure to have one. 
2. You should also have the rabbitmq instance running locally. You can run the following cmd in your terminal to have a local docker container of rabbitmq with rabbitmq-management.
    ```bash
    docker run -d --rm --name rabbitmq -p 15672:15672 -p 5672:5672 rabbitmq:3-management
    ```
3. create a virtual env with `python3 -m venv venv` and active it with `source venv/bin/activate`
4. Install the requirements with `pip install -r requirements.txt`
5. Just run the `main.py` file in the root directory and visit `http://127.0.0.1:8000/docs`