import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.preprocessing import StandardScaler

st.set_page_config(
    page_title='Clusterização', 
    layout='wide', 
    initial_sidebar_state='auto', 
    menu_items=None
)

st.title('Clusterização')
st.markdown('''
O **método do cotovelo** ajuda a encontrar o número ideal de clusters, onde o "cotovelo" no gráfico indica a melhor divisão dos dados.  
O **método da silhueta** mede a qualidade do agrupamento, onde coeficientes mais próximos de 1 indicam melhor separação entre os clusters.
''')
st.markdown('##### Aplicando o método do cotovelo, de 1 a 30 clusters:')
st.image('assets\metodo_cotovelo.png')

st.markdown('##### Aplicando o método silhueta com 3 clusters:')
st.image('assets\metodo_silhueta_3.png')

st.markdown('##### Método silhueta com 4 clusters:')
st.image('assets\metodo_silhueta_4.png')

st.markdown('##### Método silhueta com 5 clusters:')
st.image('assets\metodo_silhueta_5.png')

st.markdown('##### Método silhueta com 6 clusters:')
st.image('assets\metodo_silhueta_6.png')

st.markdown('## Análise dos Clusters')

@st.cache_data
def load_data():
    df = pd.read_csv('data/aac_intakes_outcomes.csv')

    translation_dict_animal = {
        'Dog': 'Cachorro',
        'Cat': 'Gato',
        'Bird': 'Pássaro',
        'Other': 'Outro'
    }

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

    numeric_columns = df.select_dtypes(include=['float64', 'int64'])
    scaler = StandardScaler()
    data_standardized = scaler.fit_transform(numeric_columns)
    
    return df, data_standardized

df, data_standardized = load_data()

@st.cache_data
def apply_kmeans(data, n_clusters):
    kmeans_model = KMeans(n_clusters=n_clusters, random_state=42)
    df['cluster'] = kmeans_model.fit_predict(data)
    return df

n_clusters = st.slider('Selecione o número de clusters:', 2, 10, 3)
df = apply_kmeans(data_standardized, n_clusters)

st.subheader("Distribuição dos Tipos de Animais por Cluster")
animal_dist = df.groupby(['cluster', 'animal_type']).size().reset_index(name='counts')
fig_animal_dist = px.bar(animal_dist, x='cluster', y='counts', color='animal_type', 
                         title='Distribuição dos Tipos de Animais por Cluster',
                         labels={'cluster': 'Cluster', 'counts': 'Contagem', 'animal_type': 'Tipo de Animal'})
st.plotly_chart(fig_animal_dist)

st.subheader("Idade Média dos Animais por Cluster")
age_dist = df.groupby('cluster')['age_upon_intake_(years)'].mean().reset_index()
fig_age_dist = px.bar(age_dist, x='cluster', y='age_upon_intake_(years)', 
                      title='Idade Média dos Animais por Cluster',
                      labels={'cluster': 'Cluster', 'age_upon_intake_(years)': 'Idade Média (Anos)'})
st.plotly_chart(fig_age_dist)

st.subheader("Distribuição dos Tipos de Saída por Cluster")
outcome_dist = df.groupby(['cluster', 'outcome_type']).size().reset_index(name='counts')
fig_outcome_dist = px.bar(outcome_dist, x='cluster', y='counts', color='outcome_type', 
                          title='Distribuição dos Tipos de Saída por Cluster',
                          labels={'cluster': 'Cluster', 'counts': 'Contagem', 'outcome_type': 'Tipo de Saída'})
st.plotly_chart(fig_outcome_dist)
