FROM python:3.12-slim

# Instala dependências do sistema (ajuste conforme necessário)
RUN apt-get update \
    && apt-get install -y curl build-essential libpq-dev \
    && apt-get clean

# Instala o Poetry
ENV POETRY_VERSION=1.8.2
RUN curl -sSL https://install.python-poetry.org | python3 - \
    && ln -s /root/.local/bin/poetry /usr/local/bin/poetry

# Define diretório de trabalho
WORKDIR /app

# Copia apenas arquivos de dependência
COPY pyproject.toml poetry.lock /app/

# Instala dependências do Poetry
RUN poetry config virtualenvs.create false \
    && poetry install --no-root

# Copia o restante da aplicação
COPY . /app

# Expõe a porta do Django
EXPOSE 8000

# Comando padrão
CMD ["bash", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]

