#criando uma classe 

from typing import Optional

from pydantic import BaseModel #importa o BaseModel para validar dados

class Personagem(BaseModel):
    id: Optional[int] = None
    nome: str #definiu este atributo como uma string, somente caracteres
    tipo: str 
    vida: int #definiu este atributo como int, somente números inteiros
    habilidades : str
    status : str
    imagem : str
