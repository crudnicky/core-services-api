#!/bin/bash

echo $' '  
echo $'Starting docker container for development environment'
echo $'\n--------------------------\n'
docker-compose -f docker-compose.yaml --env-file .env.dev build 
echo $'\n--------------------------\n'
docker-compose --env-file .env.dev -f docker-compose.yaml up