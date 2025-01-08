import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

st.title("Análise dos Clusters")
st.markdown('## Análise dos Clusters')
st.write("Este gráfico analisa o tempo médio que os animais passam no abrigo, segmentados por cluster.")

# Função para carregar os dados e realizar a padronização
@st.cache_data
def load_data():
    df = pd.read_csv('data/aac_intakes_outcomes.csv')

    translation_dict_animal = {
        'Dog': 'Cachorro',
        'Cat': 'Gato',
        'Bird': 'Pássaro',
        'Other': 'Outro'
    }

    # Dicionário de tradução para tipos de saída
    translation_dict_outcome = {
        'Adoption': 'Adotado',
        'Died': 'Morreu',
        'Euthanasia': 'Eutanásia',
        'Missing': 'Perdido',
        'Return to Owner': 'Retornou ao dono',
        'Transfer': 'Transferido'
    }

    df['animal_type'] = df['animal_type'].map(translation_dict_animal)
    df['outcome_type'] = df['outcome_type'].map(translation_dict_outcome)

    # Seleciona as colunas numéricas para a clusterização
    numeric_columns = df.select_dtypes(include=['float64', 'int64'])

    # Padronização dos dados
    scaler = StandardScaler()
    data_standardized = scaler.fit_transform(numeric_columns)
    
    return df, data_standardized

# Carregar os dados e realizar a padronização
df, data_standardized = load_data()

# Função para aplicar o modelo KMeans
@st.cache_data
def apply_kmeans(data, n_clusters):
    kmeans_model = KMeans(n_clusters=n_clusters, random_state=42)
    df['cluster'] = kmeans_model.fit_predict(data)
    return df

n_clusters = st.slider('Selecione o número de clusters:', 2, 10, 3)

# Aplicar o KMeans com o número de clusters selecionado
df = apply_kmeans(data_standardized, n_clusters)

# Gráfico 1: Distribuição dos Tipos de Animais por Cluster
st.subheader("Distribuição dos Tipos de Animais por Cluster")
animal_dist = df.groupby(['cluster', 'animal_type']).size().reset_index(name='counts')
fig_animal_dist = px.bar(animal_dist, x='cluster', y='counts', color='animal_type', 
                         title='Distribuição dos Tipos de Animais por Cluster',
                         labels={'cluster': 'Cluster', 'counts': 'Contagem', 'animal_type': 'Tipo de Animal'})
st.plotly_chart(fig_animal_dist)

# Gráfico 2: Distribuição dos Tipos de Saída por Cluster
st.subheader("Distribuição dos Tipos de Saída por Cluster")
outcome_dist = df.groupby(['cluster', 'outcome_type']).size().reset_index(name='counts')
fig_outcome_dist = px.bar(outcome_dist, x='cluster', y='counts', color='outcome_type', 
                          title='Distribuição dos Tipos de Saída por Cluster',
                          labels={'cluster': 'Cluster', 'counts': 'Contagem', 'outcome_type': 'Tipo de Saída'})
st.plotly_chart(fig_outcome_dist)

# Gráfico 3: Tempo Médio no Abrigo por Cluster
st.subheader("Tempo Médio no Abrigo por Cluster")
time_in_shelter_dist = df.groupby('cluster')['time_in_shelter_days'].mean().reset_index()
fig_time_dist = px.bar(time_in_shelter_dist, x='cluster', y='time_in_shelter_days', 
                      title='Tempo Médio no Abrigo por Cluster',
                      labels={'cluster': 'Cluster', 'time_in_shelter_days': 'Tempo Médio no Abrigo (dias)'})
st.plotly_chart(fig_time_dist)