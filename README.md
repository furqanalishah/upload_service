# upload_service

## Description
Upload Service is responsible for Uploading Video to the GridFS(MongoDB). After the successful upload, 
the uploaded video id (fid) will be sent to the RabbitMQ Queue that then will be consumed by the 
`converter_service`.