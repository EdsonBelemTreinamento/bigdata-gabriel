class Vacina:

    def __init__(self,id=None,vac_fabric_nome=None,municipio_nome=None,data_aplicacao=None):
        self.id = id
        self.vac_fabric_nome = vac_fabric_nome
        self.municipio_nome = municipio_nome
        self.data_aplicacao = data_aplicacao

    def __str__(self):
        return f"{self.id},{self.vac_fabric_nome},{self.municipio_nome},{self.data_aplicacao}"

    def __dict__(self):
        return {"id":self.id,
         "vac_fabric_nome":self.vac_fabric_nome,
         "municipio_nome": self.municipio_nome,
         "data_aplicacao": self.data_aplicacao
        }
