#!/bin/bash

TAG=$1

echo "Parando o container atual..."
docker stop api_container && docker rm api_container

echo "Subindo imagem $TAG"
docker run -d --name api_container -p 8000:8000 lacreisaude_api:$TAG

echo "Verificando saúde da aplicação..."
sleep 5
curl -f http://localhost:8000/health/ || {
  echo "❌ Deploy falhou, revertendo..."
  ./rollback.sh
  exit 1
}

