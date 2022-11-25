# Requests

## How to build the appache container

``` bash
docker build -t my-apache2 .
docker run -dit --name my-running-app -p 8080:80 my-apache2
```
The website is accesable at http://localhost:8080 
