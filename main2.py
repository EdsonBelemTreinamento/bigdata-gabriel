import pandas as pd

from controller.connection import session
from models.vacinas import Vacinas

'''
    Lê o arquivo CSV "dados_vacinas_v1.csv" e retorna apenas as colunas "['estabelecimento_municipio_nome', 'vacina_dataAplicacao', 'vacina_nome']"
   -proximo passo e enviar esse retorno em forma de mensagem para um producer Kafka-
'''
def dataframe_filtrado():    
    path_csv = r"C:\Users\Pc\Desktop\Programação\Python\analise_vacinas_covid\dados_vacinas_v1.csv"

    dados = pd.read_csv(path_csv, sep=';', usecols=['estabelecimento_municipio_nome', 'vacina_dataAplicacao', 'vacina_nome'], on_bad_lines='warn')

    return dados

#SELECT
data = session.query(Vacinas).all()
print(data)

session.commit()
session.close() 