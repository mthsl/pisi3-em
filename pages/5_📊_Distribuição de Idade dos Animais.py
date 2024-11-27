import streamlit as st
import pandas as pd
import plotly.express as px

st.write('<h1>Distribuição de Idade dos Animais</h1>', unsafe_allow_html=True)

df = pd.read_csv('data/aac_intakes_outcomes.csv')

age_group_column = st.selectbox(
    "Escolha o grupo de idades para exibição:",
    ["Grupo de idade no momento de entrada", "Grupo de idade no momento de saída"]
)

if age_group_column == "Grupo de idade no momento de entrada":
    age_group_col = 'age_upon_intake_(years)'
else:
    age_group_col = 'age_upon_outcome_(years)'

df[age_group_col] = pd.to_numeric(df[age_group_col], errors='coerce')
df_age = df[[age_group_col]].dropna()

# Definir as faixas etárias de 2 em 2 anos até 15 anos
bins = list(range(0, 16, 2))  # Faixas de 0-2, 2-4, 4-6, ..., 14-16
labels = [f'{i}-{i+2}' for i in bins[:-1]]  # Rótulos para as faixas etárias

df_age['age_group'] = pd.cut(df_age[age_group_col], bins=bins, labels=labels, right=False)

age_group_counts = df_age['age_group'].value_counts().sort_index().reset_index()
age_group_counts.columns = ['Faixa Etária', 'Contagem']

fig = px.bar(age_group_counts,
             x='Faixa Etária',
             y='Contagem',
             title=f'Distribuição de Idade dos Animais ({age_group_column})',
             labels={'Contagem': 'Quantidade de Animais', 'Faixa Etária': 'Faixa Etária (Anos)'},
             color='Faixa Etária')

fig.update_layout(barmode='group', xaxis_title="Faixa Etária", yaxis_title="Quantidade de Animais", showlegend=False)

st.plotly_chart(fig)