import streamlit as st
import pandas as pd
import plotly.express as px

st.write('<h1>Distribuição do Tempo no Abrigo por Tipo de Entrada</h1>', unsafe_allow_html=True)

df = pd.read_csv('data/aac_intakes_outcomes.csv')

df_filtered = df[['intake_type', 'time_in_shelter_days']]

df_filtered = df_filtered.dropna(subset=['time_in_shelter_days'])

df_filtered['intake_type'] = df_filtered['intake_type'].replace({
    'Stray': 'Animal de Rua',
    'Owner Surrender': 'Desistência do Tutor',
    'Public Assist': 'Assistência Pública', 
    'Euthanasia Request': 'Requisição de Eutanásia', 
    'Wildlife': 'Animal Selvagem' 
})

fig = px.scatter(
    df_filtered,
    x='intake_type',
    y='time_in_shelter_days',
    title='Distribuição do Tempo no Abrigo por Tipo de Entrada',
    labels={'intake_type': 'Tipo de Entrada', 'time_in_shelter_days': 'Tempo no Abrigo (dias)'},
    color='intake_type',
    category_orders={'intake_type': ['Animal de Rua', 'Desistência do Tutor', 'Assistência Pública', 
                                     'Requisição de Eutanásia', 'Animal Selvagem']},
    width=800,  # Definir a largura do gráfico
    height=500  # Definir a altura do gráfico
)

fig.update_layout(
    title={'text': 'Distribuição do Tempo no Abrigo por Tipo de Entrada', 'x': 0.5, 'xanchor': 'center'},
    xaxis=dict(title='Tipo de Entrada'),
    yaxis=dict(title='Tempo no Abrigo (dias)'),
    plot_bgcolor='rgba(0,0,0,0)',  # Fundo transparente
    paper_bgcolor='rgba(0,0,0,0)',  # Fundo da área do gráfico transparente
    font=dict(family="Arial", size=12, color="black"),
    showlegend=True
)

st.plotly_chart(fig)