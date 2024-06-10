from typing import Union
from fastapi import FastAPI
from vacina import Vacina
from vacina_repository import  VacinaTB, VacinaRepository
from pydantic import BaseModel

app = FastAPI()
repository = VacinaRepository()

class ItemVacina(BaseModel):
    vac_fabric_nome: str
    municipio_nome: str
    data_aplicacao: str


@app.get("/api/vacina/{id}")
def buscar_por_id(id: int):
    try:
        results =  repository.buscar_por_id(id)
        return results
    except Exception as error:
        return {"message":"nao Encontrado"}

@app.get("/api/vacinas")
def buscar_todos():
    try:
        results =   repository.buscar_todos()
        return results
    except Exception as error:
        return {"message":"nao Encontrado"}
    

@app.post("/api/gravar")
def gravar(item: ItemVacina):
    return repository.create_vacina(item)




