# dockers-viasat
## Problem for Viasat
Problem statement - Bring up 2 dockers in a vm, 1 running the webserver and the other running mysql db. Any post transaction has to go from webClient to Docker 1 (webserver) to Docker2(mysql).

## Why the problem was chosen?
I wanted to work in backend side more, especially deployment side. The problem seemed most appropriate for the role I wanted. 

## Things learnt during mini problem
1. Learnt how dockers work. Dockers make life of programmers so easy :smiley:.
2. Relearnt the PostgreSQL and Flask.
3. Learnt to not overestimate myself and try to be more systematic in future.

## Major command used
Docker build command:

`docker build name_of_container:latest .`


Docker network setup:

`docker network create --subnet=172.18.0.0/16 mynet123`


Docker run command:

`docker run --net mynet123 --ip 172.18.0.8 -p 5000:5000 name_of_container`


Docker exec command:

`docker exec -it name_of_container /bin/bash`


## Work which could have been done

1. I assigned IP address of the PostgreSQL server as a hard coded value. It could have been handled more elegantly with the help of service registry.
2. I could have learnt Kubernetes as well.
