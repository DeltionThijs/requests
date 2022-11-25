# Requests

## How to build the appache container manuallt

``` bash
docker build -t my-apache2 .
docker run -dit --name my-running-app -p 8080:80 my-apache2
```
The website is accesable at http://localhost:8080 

## Confirming the requests from container

Use the docker conainer logs from apache server for testing the requests that are send

https://github.com/docker/docker-py

From this we can import the library and use that to programmaticly run and use docker containers with python.
