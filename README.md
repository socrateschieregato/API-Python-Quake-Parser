**Parser**

Parser de logs do game Quake que retorna os resultados das partidas

**Instalação**
Após realizar a clonagem do projeto, entre na projeto da aplicação e execute os códigos abaixo no cmd/shell para instalar as dependências do webserver.

1º pip install -r requirements.txt

2º python manage.py runserver

**Rotas**
LISTAR GAMES(Todos)

GET /api/v1/games

Exemplo:

{

"game_1": {
    "total_kills": 0,
    "players": [
        "Isgalamido"
    ],
    "kills": {
        "Isgalamido": 0
    }
},

"game_2": {
    "total_kills": 11,
    "players": [
        "Isgalamido",
        "Mocinha"
    ],
    "kills": {
        "Isgalamido": 4,
        "Mocinha": 0
    }
}
}

**Buscar um game especídfico**

Retorna um game específico a partir de um ID informado

POST /api/v1/games/{id}

Exemplo:

{

"total_kills": 14,

    "players": [
    
        "Zeh",
        "Isgalamido",
        "Zeh",
        "Assasinu Credi"
        
    ],
    "kills": {
    
        "Zeh": 0,
        "Isgalamido": 2,
        "Assasinu Credi": 1
        }
}

**Executando os testes**
A aplicação foi testada usando pytest, para executar a rotina de testes, basta digitar o comando abaixo no cmd/shell.

pytest

