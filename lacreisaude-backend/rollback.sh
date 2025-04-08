#!/bin/bash

echo "Revertendo para a imagem anterior..."
docker stop api_container && docker rm api_container
docker run -d --name api_container -p 8000:8000 lacreisaude_api:previous_tag

