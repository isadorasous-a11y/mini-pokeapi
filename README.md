# Mini-PokeAPI (FastAPI + SQLAlchemy + Alembic + Docker)

API inspirada na PokéAPI, com CRUD de pokémons, paginação e deploy no Render.

## Links
- **Produção (Render):** [https://mini-pokeapi.onrender.com](https://mini-pokeapi.onrender.com)
- **Docs (Swagger):** [https://mini-pokeapi.onrender.com/docs](https://mini-pokeapi.onrender.com/docs)
- **Healthcheck:** [https://mini-pokeapi.onrender.com/healthz](https://mini-pokeapi.onrender.com/healthz)

## Tecnologias
- FastAPI
- SQLAlchemy 2
- Alembic (migrations)
- Pydantic v2
- Uvicorn
- Pytest
- Docker
- PostgreSQL (Neon) na produção

## Endpoints principais
- `GET /healthz` - Verifica se a API está online.
- `GET /pokemons?limit=&offset=&q=` - Lista de pokémons com paginação e filtro.
- `GET /pokemons/{id}` - Detalhes de um pokémon específico.
- `POST /pokemons` - Cria um novo pokémon.
- `PUT /pokemons/{id}` - Atualiza as informações de um pokémon.
- `DELETE /pokemons/{id}` - Exclui um pokémon.


## Execução local (SQLite)
Para rodar o projeto localmente com **SQLite**:

1. Crie e ative o ambiente virtual:
   ```bash
   python -m venv .venv
   # PowerShell (Windows):
   . .\.venv\Scripts\Activate.ps1

2. Instale as dependências:
pip install -r requirements.txt

3. Rode as migrations para criar as tabelas no banco de dados:
alembic upgrade head

4. Inicie o servidor:
uvicorn app.main:app --reload  # Acesse http://127.0.0.1:8000/docs

## Execução com Docker (PostgreSQL)
1. Certifique-se de que o Docker está instalado e rodando.
2. Construa e suba os containers:
docker compose up --build
3. Acesse a API através de http://localhost:8000/docs

## Variáveis de ambiente
A API utiliza o arquivo .env para configurar as variáveis de ambiente. Exemplo de como criar o arquivo .env:
DATABASE_URL=postgresql://USER:SENHA@HOST:5432/DB?sslmode=require

## Estrutura do Projeto
A estrutura do projeto é a seguinte:
app/
  main.py         # Inicialização da aplicação FastAPI
  models.py       # Definições dos modelos de dados
  schemas.py      # Schemas Pydantic para validação de dados
  crud.py         # Funções de manipulação de dados
  db.py           # Conexão com o banco de dados
  routers/
    pokemons.py   # Rotas de pokémons
alembic/
  env.py           # Configuração do Alembic
  versions/        # Diretório das migrations
Dockerfile         # Dockerfile para criação da imagem
docker-compose.yml # Configuração do Docker Compose
requirements.txt   # Dependências do projeto
README.md          # Documentação do projeto
tests/             # Testes da aplicação
  test_health.py   # Testes para verificar a saúde da API
  test_pokemons.py # Testes CRUD para a API de pokémons
LICENSE            # Licença do projeto    

## Rodando o script de "Seed" (opcional)
1. Defina a variável de ambiente DATABASE_URL (para apontar para o seu banco de dados):
export DATABASE_URL=postgresql://USER:SENHA@HOST:5432/DB?sslmode=require
2. Rode o script de seed:
python -m scripts.seed

## Testes
Para rodar os testes da aplicação:
pytest -q

Se quiser gerar um relatório de cobertura de código:
coverage run -m pytest -q 
coverage report -m

## Licença

Este projeto está licenciado sob a **MIT License**. Veja o arquivo [LICENSE](./LICENSE) para mais detalhes.