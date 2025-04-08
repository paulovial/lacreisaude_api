# Lacrei Saúde - Backend API

## Sumário
- [Visão Geral](#visão-geral)
- [Stack Tecnológica](#stack-tecnológica)
- [Setup do Ambiente Local](#setup-do-ambiente-local)
- [Setup com Docker](#setup-com-docker)
- [Execução do Projeto](#execução-do-projeto)
- [Testes Automatizados](#testes-automatizados)
- [Healthcheck](#healthcheck)
- [Decisões Técnicas](#decisões-técnicas)
- [Deploy e CI/CD](#deploy-e-cicd)
- [Erros Encontrados e Melhorias Propostas](#erros-encontrados-e-melhorias-propostas)

## Visão Geral

API RESTful desenvolvida para gestão de consultas médicas, como parte do desafio técnico da Lacrei Saúde. O sistema permite cadastro de profissionais de saúde, registro de consultas, e simulação de pagamentos.

## Stack Tecnológica

- Python 3.12
- Django 5.2
- Django REST Framework
- PostgreSQL
- Docker / Docker Compose
- Poetry (gerenciador de dependências)
- GitHub Actions (CI)
- AWS EC2 (Staging/Produção)

## Setup do Ambiente Local

1. Clone o repositório:

```bash
git clone <url-do-repo>
cd lacreisaude-backend
```

2. Crie e ative um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate
```

3. Instale as dependências:

```bash
poetry install
```

4. Configure o banco de dados PostgreSQL local e o `.env` (caso necessário).

5. Rode as migrações:

```bash
python manage.py migrate
```

6. Execute o servidor:

```bash
python manage.py runserver
```

## Setup com Docker

1. Construa e inicie os containers:

```bash
docker-compose up --build
```

2. O backend estará acessível em `http://localhost:8000`.

## Execução do Projeto

- Endpoint de healthcheck: `GET /api/health/`
- Cadastro e listagem de profissionais: `GET/POST /api/profissionais/`
- Registro de consultas: `GET/POST /api/consultas/`
- Mock de pagamento: `POST /api/pagamentos/mock/`

## Testes Automatizados

Os testes utilizam `APITestCase` do Django REST Framework. Para executá-los:

```bash
python manage.py test
```

Ou, caso esteja usando o Poetry:

```bash
poetry run python manage.py test
```

## Healthcheck

O endpoint `/api/health/` foi adicionado ao projeto principal para verificação do status da aplicação. Ele retorna `200 OK` com um JSON simples:

```json
{"status": "ok"}
```

## Decisões Técnicas

- Django + DRF: escolhidos por serem frameworks maduros, com excelente suporte para construção rápida de APIs REST.
- Poetry: facilita o gerenciamento de dependências e ambientes isolados.
- Docker: usado para garantir portabilidade e padronização entre ambientes.
- GitHub Actions: CI com lint, build da imagem Docker e execução de testes automatizados.
- AWS EC2: instâncias para staging e produção, utilizando `docker-compose` para orquestração.

## Deploy e CI/CD

- O repositório possui o arquivo `.github/workflows/ci.yml`, que automatiza testes e build da imagem.
- Scripts `deploy.sh` e `rollback.sh` foram criados para facilitar publicação e reversão de versões.
- A aplicação é exposta na porta `8000` da instância EC2.
- Backups do banco de dados são gerados via `pg_dump` dentro do container PostgreSQL.

## Erros Encontrados e Melhorias Propostas

### Erros Corrigidos

- DisallowedHost: resolvido adicionando `localhost` e IP público à lista `ALLOWED_HOSTS`.
- 404 em healthcheck: problema de roteamento corrigido ao mover `health.py` para o diretório correto e ajustar `urls.py`.
- Permissões no endpoint de pagamento: validado o uso correto de `@api_view` e `@permission_classes`.
- Backup falhando: erro de autenticação corrigido ao usar o nome correto do role no PostgreSQL.

### Melhorias Futuras

- Integração real com o Asaas (atualmente é um mock baseado na documentação).
- Uso de variáveis de ambiente centralizadas com suporte a `.env` nos ambientes.
- Implementar autenticação com JWT.
- Adicionar versão de staging automatizada via CI/CD.
- Cobertura de testes com relatório (ex: cobertura com `coverage.py`).

---

Este projeto foi desenvolvido como parte de um desafio técnico. Todos os aspectos práticos foram documentados, visando clareza, rastreabilidade e reprodutibilidade.


