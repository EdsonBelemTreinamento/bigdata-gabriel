import streamlit as st
import pandas as pd
import plotly.express as px

dados = {
    'id_vac': [1, 2, 3, 4, 5],
    'vac_fabric_nome': ['ravac', 'ragnarok', 'ravac', 'ravanoque', 'ragnarok'],
    'municipio_nome': ['nova Iguacu', 'Mesquita', 'nova Iguacu', 'nova Iguacu', 'Mesquita'],
    'data_aplicacao': ['2022-10-01', '2022-12-01', '2022-10-01', '2022-11-01', '2022-12-01']
}
df = pd.DataFrame(dados)

colors_sus = ['#00A7E1', '#FFD100', '#9EAEC0']  # Azul, Amarelo, Cinza

st.title('Dashboard de Vacinação')

tipo_grafico = st.sidebar.radio('Escolha o tipo de gráfico:', ['Contagem por Fabricante e Município', 'Tendência por Data de Aplicação', 'Distribuição por Fabricante'])

st.subheader('Dados Gerais')
st.dataframe(df)

if st.sidebar.button('Gerar Gráfico'):
    if tipo_grafico == 'Contagem por Fabricante e Município':
        st.subheader('Contagem por Fabricante e Município')
        fig_contagem = px.bar(df, x='vac_fabric_nome', color='municipio_nome', title='Contagem de Vacinas por Fabricante e Município', color_discrete_sequence=colors_sus)
        st.plotly_chart(fig_contagem)
        
    elif tipo_grafico == 'Tendência por Data de Aplicação':
        st.subheader('Tendência por Data de Aplicação')
        fig_tendencia = px.line(df, x='data_aplicacao', title='Tendência de Aplicação de Vacinas ao Longo do Tempo', color_discrete_sequence=[colors_sus[0]])
        st.plotly_chart(fig_tendencia)
        
    elif tipo_grafico == 'Distribuição por Fabricante':
        st.subheader('Distribuição por Fabricante')
        fig_distribuicao = px.pie(df, values=df.groupby('vac_fabric_nome')['id_vac'].count(), names=df['vac_fabric_nome'].unique(), title='Distribuição de Vacinas por Fabricante', color_discrete_sequence=colors_sus)
        st.plotly_chart(fig_distribuicao)
