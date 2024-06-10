# from datetime import datetime, timedelta
from sqlalchemy import create_engine, Column, String, DateTime, Integer
from sqlalchemy.orm import sessionmaker,declarative_base
from vacina import Vacina
import json

# ORM da Classe ele gera a tabela


Base = declarative_base()

class VacinaTB(Base):
    __tablename__="vacinas2"
    id = Column(Integer, primary_key=True)
    vac_fabric_nome = Column(String(100), nullable=False)
    municipio_nome = Column(String(100), nullable=False)
    data_aplicacao = Column(String(100), nullable=False)

    #date_created= Column(DateTime)


class VacinaRepository:
    def __init__(self):
        self.engine = create_engine('postgresql://postgres:root1@localhost:5432/gab')
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
    
    def create_vacina(self, vacina ):
        session = self.Session()
        vacinaobj = VacinaTB(vac_fabric_nome = vacina.vac_fabric_nome ,municipio_nome = vacina.municipio_nome, data_aplicacao=vacina.data_aplicacao)
        session.add(vacinaobj)
        session.commit()

    def buscar_por_id(self, vacina_id):
        session = self.Session()
        vacina = session.query(VacinaTB).filter_by(id=vacina_id).first()
        if vacina:
             return json.dumps(vacina.__dict__())
        else:
            return None
    
    def buscar_todos(self):
        session = self.Session()
        vacinas = session.query(VacinaTB).all()
        vacinas_data = []
        for vacina in vacinas:
            vacinas_data.append(json.dumps({
                'id': vacina.id,
                'vac_fabric_nome': vacina.vac_fabric_nome,
                'municipio_nome': vacina.municipio_nome,
                'data_aplicacao': vacina.data_aplicacao
            }))
        return vacinas_data
            

#if __name__=="__main__":
   # try:
   #     vacina1= Vacina(vac_fabric_nome="ravac",municipio_nome="nova Iguacu",data_aplicacao="2022-10-01")
   #     vacina2= Vacina(vac_fabric_nome="ravanoque",municipio_nome="nova Iguacu",data_aplicacao="2022-11-01")
   #     vacina3= Vacina(vac_fabric_nome="ragnarok",municipio_nome="Mesquita",data_aplicacao="2022-12-01")
   #     repository = VacinaRepository()
   #     repository.create_vacina(vacina1)
   #     repository.create_vacina(vacina2)
   #     repository.create_vacina(vacina3)
   #     print("############################# Buscar UM")
   #     print (repository.buscar_por_id(9))
   #     print(".")
   #     print(".")
   #     print(".")
   #     print("############################# Buscar Todos")
   #     print( repository.buscar_todos() )
   #     print("####################### FIm ")
   # except Exception as error:
   #     print(f"{error}")

