from pydantic import BaseModel

class Usuario (BaseModel):
  nome: str
  idade: int
  ativo: bool = True

try: 
 usuario = Usuario(nome="João", idade=30)
 print(usuario.idade)
 print(type(usuario))
except Exception as e:
  print(f"Ocorreu um erro: {e}")