import streamlit as st
import pandas as pd
import plotly.express as px

st.write('<h1>Condição de Entrada por Tipo de Animal</h1>', unsafe_allow_html=True)

df = pd.read_csv('data/aac_intakes_outcomes.csv')

df_bar = df[['animal_type', 'intake_condition']].copy()

df_bar['animal_type'] = df_bar['animal_type'].replace({
    'Bird': 'Pássaro', 'Cat': 'Gato', 'Dog': 'Cachorro', 'Other': 'Outros'
})

df_bar['intake_condition'] = df_bar['intake_condition'].replace({
    'Aged': 'Idoso', 'Feral': 'Feroz', 'Injured': 'Machucado', 'Normal': 'Normal',
    'Nursing': 'Amamentando', 'Other': 'Outros', 'Pregnant': 'Grávida', 'Sick': 'Doente'
})

df_bar_grouped = df_bar.groupby(['animal_type', 'intake_condition']).size().reset_index(name='count')

fig_bar = px.bar(
    df_bar_grouped,
    x='animal_type',
    y='count',
    color='intake_condition',
    title='Distribuição de Condições de Entrada por Tipo de Animal',
    labels={
        'animal_type': 'Tipo de Animal',
        'intake_condition': 'Condição de Entrada',
        'count': 'Contagem'
    },
    color_discrete_map={
        'Idoso': '#D62728',  # Vermelho escuro
        'Feroz': '#1F77B4',  # Azul escuro
        'Machucado': '#2CA02C',  # Verde escuro
        'Normal': '#9467BD',  # Roxo
        'Amamentando': '#FF7F0E',  # Laranja
        'Outros': '#E377C2',  # Rosa
        'Grávida': '#FFBB78',  # Amarelo claro
        'Doente': '#8C564B'  # Marrom
    },
    barmode='stack'
)

fig_bar.update_layout(
    xaxis=dict(title='Tipo de Animal'),
    yaxis=dict(title='Contagem')
)

st.plotly_chart(fig_bar)
