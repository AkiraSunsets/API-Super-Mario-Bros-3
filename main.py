from fastapi import FastAPI, HTTPException, status, Depends
from typing import Optional, Any
from model import Personagem

app = FastAPI(
    title="Super Mario Bros 3", 
    version="0.0.1", 
    description="Confira abaixo os personagens do jogo Super Mario Bros 3"
    )

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

    6: {
        "nome" : "Toad",
        "tipo" : "NPC",
        "vida" : None,
        "habilidades" : [],
        "status" : "npc",
        "imagem" : "https://github.com/AkiraSunsets/API-Super-Mario-Bros-3/blob/main/Mario%20Characters/toad.jpg"
    }

}

#CREATE
@app.post("/personagens", response_model=Personagem, status_code=status.HTTP_201_CREATED, tags=["Personagens: "], summary="Criar novo personagem")
async def criar_personagem(personagem: Personagem):
    if personagem.id in personagens:
        raise HTTPException(status_code=400, detail="ID já existe")
    
    #converte o objeto Pydantic em dicionário e salva no "banco"
    personagens[personagem.id] = personagem.dict() 
    return personagem
#=============================================================

#read all
@app.get("/personagens", tags=["Personagens: "], summary="Listar todos os personagens da API") #categoria com nome opcional
async def get_personagens(db: Any = Depends(fake_db)): #verifica se há pelo menos um item verdadeiro
    return personagens

#read one
@app.get("/personagens/{personagem_id}", description="Retorna um personagem com um id especifico", tags=["Personagens: "], summary="Pesquisa pela o ID")
async def get_personagem(personagem_id: int): #usado no singular para realizar uma busca de um unico id
    try:
        personagem = personagens[personagem_id] 
        return personagem
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Este personagem não foi encontrado")
#===================================================================

#UPDATE
@app.put("/personagens/{personagem_id}", response_model=Personagem, tags=["Personagens: "], summary= "Atualiza personagem")
async def atualizar_personagem(personagem_id: int, personagem: Personagem):

    #Se o personagem não existir no banco, tem como atualizar
    if personagem_id not in personagens:
        raise HTTPException(status_code=404, detail="Personagem não encontrado")
    

    #substitui o personagem antigo pelos novos dados
    personagens[personagem_id] = personagem.dict()

    #retorna o personagem atualizado
    return personagem
#=============================================================

#DELETE
@app.delete ("/personagens/{personagem_id}", status_code=status.HTTP_200_OK, tags=["Personagens: "], summary="Deletar personagens")
async def deletar_personagens(personagem_id: int):

    #verifica se o personagem existe

    if personagem_id not in personagens:
        raise HTTPException(status_code=404, detail="Personagem não encontrado")
    

    #remove o personagem
    del personagens[personagem_id]

    #return messagem de sucesso
    return {"msg": "Personagem deletado com sucesso"}


#===========================RUN=====================================
if __name__ == '__main__':
    import uvicorn #é usado para que se houver a necessidade 
                   #de realizar alguma alteração de alguma informação na execução do código
    uvicorn.run("main:app", host="127.0.0.1", port=8003, reload=True)