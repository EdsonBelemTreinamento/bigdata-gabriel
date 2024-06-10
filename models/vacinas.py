from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class Vacinas(Base):
    __tablename__ = "vacinas"

    id_vac = Column(Integer, primary_key=True)
    vac_fabric_nome = Column(String(100), nullable=False)
    municipio_nome = Column(String(100), nullable=False)
    data_aplicacao = Column(String(100), nullable=False)

    def __repr__(self):
        return f"Vacina (fabricante={self.vac_fabric_nome}, municipio={self.municipio_nome})"
