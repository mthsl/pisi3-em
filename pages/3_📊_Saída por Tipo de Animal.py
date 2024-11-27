import streamlit as st
import pandas as pd
import plotly.express as px

st.write('<h1>Condições de Saída por Tipo de Animal</h1>', unsafe_allow_html=True)

df = pd.read_csv('data/aac_intakes_outcomes.csv')

animal_type_column = 'animal_type'
outcome_type_column = 'outcome_type'

translation_dict_animal = {
    'Dog': 'Cachorro',
    'Cat': 'Gato',
    'Bird': 'Pássaro',
    'Other': 'Outro'
}
translation_dict_outcome = {
    'Adoption': 'Adotado',
    'Euthanasia': 'Eutanasiado',
    'Transfer': 'Transferido',
    'Died': 'Falecido',
    'Return to Owner': 'Retornado ao Dono',
    'Disposal': 'Descartado',
    'Missing': 'Desaparecido',
    'Relocate': 'Realocado',
    'Rto-Adopt': 'Retornado e Adotado'
}

df[animal_type_column] = df[animal_type_column].map(translation_dict_animal)
df[outcome_type_column] = df[outcome_type_column].map(translation_dict_outcome)

df_cleaned = df[[animal_type_column, outcome_type_column]].dropna()

excluded_outcomes = ['Descartado', 'Realocado', 'Retornado e Adotado']
df_cleaned = df_cleaned[~df_cleaned[outcome_type_column].isin(excluded_outcomes)]

selected_animal = st.selectbox(
    "Selecione o Tipo de Animal:",
    ['Todos', 'Cachorro', 'Gato', 'Pássaro', 'Outro']
)

if selected_animal != 'Todos':
    df_cleaned = df_cleaned[df_cleaned[animal_type_column] == selected_animal]

outcome_counts = df_cleaned.groupby([outcome_type_column, animal_type_column]).size().reset_index(name='count')

fig = px.bar(outcome_counts,
             x=outcome_type_column,
             y='count',
             color=animal_type_column,
             title='Condições de Saída por Tipo de Animal',
             labels={'count': 'Quantidade de Animais', outcome_type_column: 'Condição de Saída', animal_type_column: 'Tipo de Animal'},
             barmode='group')

fig.update_layout(xaxis_title="Condição de Saída", yaxis_title="Quantidade de Animais")

st.plotly_chart(fig)
