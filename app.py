import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Usuario (BaseModel):
  nome: str
  idade: int
  ativo: bool = True

@app.get("/saudar{nome}")
async def saudar(nome: str):
    return {"mensagem": f"Olá, {nome}!"}

@app.post("/usuarios")
async def criar_usuario(usuario: Usuario):
  return{
     "mensagem": f"Usuário {usuario.nome} criado com sucesso!",
     "dados": dict(usuario)
  }

if __name__ == "__main__":
    uvicorn.run(
      "app:app",
      host="0.0.0.0",
      port=3001,
      reload=True
    )

  #Servidor
  #Tipagem
  #Assincronismo ###### IMPORTANTE
  #Doc