from fastapi import FastAPI, HTTPException, status, Depends
from routes import personagens_router, usuario_router #faz com que o FASTAPI importe as rotas
from typing import Optional, Any

app = FastAPI(title="Super Mario Bros 3", version="0.0.1", description="Confira abaixo os personagens do jogo Super Mario Bros 3")

app.include_router(personagens_router.router, tags=['personagens']) #faz com que seja incluido as rotas 

def fake_db():
    try:
        print("Connecting to the bank")
    finally:
        print("Closing the bank")


personagens = { #foi criado um json para funcionar como armazenamento
    1: { 
        "nome": "Mario Bros",
        "tipo" : "Jogador",
        "vida" : 5,
        "habilidades" : ["Pulo alto", "Pulo duplo", "Correr rápido", "voar"],
        "status" : "disponível",
        "imagem" : "https://github.com/AkiraSunsets/API-Super-Mario-Bros-3/blob/main/Mario%20Characters/mario.jpg"
    },
    
    2: {
        "nome" : "Luigi Bros",
        "tipo" : "Jogador",
        "vida" : 5,
        "habilidades" : ["Pulo alto", "Pulo duplo", "Correr rápido", "voar"],
        "status" : "disponível",
        "imagem" : "https://github.com/AkiraSunsets/API-Super-Mario-Bros-3/blob/main/Mario%20Characters/luigi.jpg"
    },

    3: {
        "nome" : "Princess Peach",
        "tipo" : "NPC",
        "vida" : None,
        "habilidades" : [],
        "status" : "npc",
        "imagem" : "https://github.com/AkiraSunsets/API-Super-Mario-Bros-3/blob/main/Mario%20Characters/princess.peach.jpg"
    },

    4: {
        "nome" : "Bowser",
        "tipo" : "Inimigo",
        "vida" : 3,
        "habilidades" : ["Sopro de fogo", "Força bruta", "Arremesso de bombas/balas"],
        "status" : "inimigo",
        "imagem" : "https://github.com/AkiraSunsets/API-Super-Mario-Bros-3/blob/main/Mario%20Characters/bowser.jpg"
    },

    5: {
        "nome" : "Koopa Troopa",
        "tipo" : "Inimigo",
        "vida" : 2,
        "habilidades" : ["Andar rápido", "Esconder na casca"],
        "status" : "inimigo",
        "imagem" : "https://github.com/AkiraSunsets/API-Super-Mario-Bros-3/blob/main/Mario%20Characters/koopa.troopa.jpg"
    },

        5: {
        "nome" : "Toad",
        "tipo" : "NPC",
        "vida" : None,
        "habilidades" : [],
        "status" : "npc",
        "imagem" : "https://github.com/AkiraSunsets/API-Super-Mario-Bros-3/blob/main/Mario%20Characters/toad.jpg"
    }

}

@app.get("/")
async def raiz():
    return{"API - Personagens Super Mario Bros 3"} #funciona como o main

@app.get("/personagens") #categoria com nome opcional
async def get_personagens(db: Any = Depends(fake_db)): #verifica se há pelo menos um item verdadeiro
    return personagens

@app.get("/personagens/{personagem_id}", description="Retorna um personagem com um id especifico")
async def get_personagem(personagem_id: int): #usado no singular para realizar uma busca de um unico id
    try:
        personagem = personagens[personagem_id] 
        return personagem
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Este personagem não foi encontrado")
    

if __name__ == '__main__':
    import uvicorn #é usado para que se houver a necessidade 
                   #de realizar alguma alteração de alguma informação na execução do código
    uvicorn.run("main:app", host="127.0.0.1", port=8002, reload=True)

