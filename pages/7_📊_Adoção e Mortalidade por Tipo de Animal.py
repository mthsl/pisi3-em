import streamlit as st
import pandas as pd
import plotly.express as px

# Título da Página
st.write('<h1>Análise de Adoção e Mortalidade por Tipo de Animal</h1>', unsafe_allow_html=True)

# Carregar os dados
df = pd.read_csv('data/aac_intakes_outcomes.csv')

# Filtrar apenas colunas relevantes
df_filtered = df[['animal_type', 'outcome_type']]

# Limpar valores ausentes
df_filtered = df_filtered.dropna(subset=['animal_type', 'outcome_type'])

# Traduzir os tipos de saída
df_filtered['outcome_type'] = df_filtered['outcome_type'].replace({
    'Adoption': 'Adotado',
    'Euthanasia': 'Eutanasiado',
    'Died': 'Falecido',
    'Return to Owner': 'Retornado ao Tutor',
    'Transfer': 'Transferido',
    'Rto-Adopt': 'Retornado para Adoção',
    'Missing': 'Desaparecido',
    'Disposal': 'Descarte'
})

# Traduzir os tipos de animais
df_filtered['animal_type'] = df_filtered['animal_type'].replace({
    'Dog': 'Cachorro',
    'Cat': 'Gato',
    'Bird': 'Pássaro',
    'Other': 'Outro'
})

# Remover os tipos de saída indesejados
df_filtered = df_filtered[~df_filtered['outcome_type'].isin(['Retornado ao Tutor', 'Transferido', 'Retornado para Adoção', 'Desaparecido', 'Descarte'])]

# Adicionar filtro interativo para o tipo de animal
selected_animal_type = st.selectbox(
    'Selecione o Tipo de Animal:',
    options=df_filtered['animal_type'].unique(),
    index=0
)

# Filtrar os dados com base no tipo de animal selecionado
df_filtered = df_filtered[df_filtered['animal_type'] == selected_animal_type]

# Contar a quantidade de adoções e mortes
counts = df_filtered['outcome_type'].value_counts().reset_index()
counts.columns = ['Tipo de Saída', 'Quantidade']

# Criar o gráfico de pizza com cores distintas
fig = px.pie(
    counts,
    names='Tipo de Saída',
    values='Quantidade',
    title=f'Porcentagem de {selected_animal_type}s Adotados e Eutanasiados',
    color='Tipo de Saída',
    color_discrete_map={
        'Adotado': 'green',
        'Eutanasiado': 'red',
        'Falecido': 'orange'
    }
)

fig.update_layout(
    title={'text': f'Porcentagem de {selected_animal_type}s Adotados e Eutanasiados', 'x': 0.5, 'xanchor': 'center'},
    font=dict(family="Arial", size=12, color="black"),
    showlegend=True
)

# Mostrar o gráfico
st.plotly_chart(fig)

# Exibir uma tabela com os dados
st.write("**Dados Agregados:**")
st.dataframe(counts)

# Nota explicativa sobre a remoção de colunas
st.write(""" 
Para simplificar a análise, algumas categorias de saída foram removidas:  
- **'Return to Owner'** e **'Transfer'**: Estas categorias não representam adoções, portanto, não são relevantes para o foco da análise.  
- **'Rto-Adopt'**, **'Missing'** e **'Disposal'**: Quantidades não impactavam de forma significativa os resultados.  

O objetivo é garantir que os dados sejam claros e relevantes, focando nos casos de adoção e eutanásia.
""")
