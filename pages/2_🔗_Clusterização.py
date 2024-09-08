import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

st.set_page_config(
    page_title='Clusterização', 
    layout='wide', 
    initial_sidebar_state='auto', 
    menu_items=None)

st.title('Clusterização')
st.markdown('#### Métodos')
st.markdown('##### Aplicando o método do cotovelo:')

st.code('''
# Remover colunas de data/hora antes de aplicar o KMeans
data_standardized = data_standardized.select_dtypes(include=['float64', 'int64'])

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Lista para armazenar a soma dos quadrados dentro dos clusters (WCSS)
wcss = []

# Testar diferentes números de clusters, por exemplo, de 1 a 30 clusters
for i in range(1, 30):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=42)
    kmeans.fit(data_standardized)
    wcss.append(kmeans.inertia_)

# Plotar o gráfico do cotovelo
plt.plot(range(1, 30), wcss, marker='o')
plt.title('Método do Cotovelo')
plt.xlabel('Número de Clusters')
plt.ylabel('WCSS')
plt.show()
''')

st.image('assets\metodo_cotovelo.png')

st.markdown('##### Aplicando o método silhueta com 3 clusters:')

st.code('''
from yellowbrick.cluster import SilhouetteVisualizer
from sklearn.cluster import KMeans

# Definir o número de clusters
n_clusters = 3

# Criar o modelo KMeans
kmeans_model = KMeans(n_clusters=n_clusters, init='k-means++', n_init=10, max_iter=300, random_state=42)

# Visualizador de silhueta usando o modelo KMeans
visualizer = SilhouetteVisualizer(kmeans_model, colors='yellowbrick')

# Ajuste o visualizador ao data_standardized
visualizer.fit(data_standardized)

visualizer.show()
''')

st.image('assets\metodo_silhueta_3.png')

st.markdown('##### Método silhueta com 4 clusters:')

st.code('''
from yellowbrick.cluster import SilhouetteVisualizer
from sklearn.cluster import KMeans

# Definir o número de clusters
n_clusters = 4

# Criar o modelo KMeans
kmeans_model = KMeans(n_clusters=n_clusters, init='k-means++', n_init=10, max_iter=300, random_state=42)

# Visualizador de silhueta usando o modelo KMeans
visualizer = SilhouetteVisualizer(kmeans_model, colors='yellowbrick')

# Ajuste o visualizador ao data_standardized
visualizer.fit(data_standardized)

visualizer.show()
''')

st.image('assets\metodo_silhueta_4.png')

st.markdown('##### Método silhueta com 5 clusters:')

st.code('''
from yellowbrick.cluster import SilhouetteVisualizer
from sklearn.cluster import KMeans

# Definir o número de clusters
n_clusters = 5

# Criar o modelo KMeans
kmeans_model = KMeans(n_clusters=n_clusters, init='k-means++', n_init=10, max_iter=300, random_state=42)

# Visualizador de silhueta usando o modelo KMeans
visualizer = SilhouetteVisualizer(kmeans_model, colors='yellowbrick')

# Ajuste o visualizador ao data_standardized
visualizer.fit(data_standardized)

visualizer.show()
''')

st.image('assets\metodo_silhueta_5.png')

st.markdown('##### Método silhueta com 6 clusters:')

st.code('''
from yellowbrick.cluster import SilhouetteVisualizer
from sklearn.cluster import KMeans

# Definir o número de clusters
n_clusters = 6

# Criar o modelo KMeans
kmeans_model = KMeans(n_clusters=n_clusters, init='k-means++', n_init=10, max_iter=300, random_state=42)

# Visualizador de silhueta usando o modelo KMeans
visualizer = SilhouetteVisualizer(kmeans_model, colors='yellowbrick')

# Ajuste o visualizador ao data_standardized
visualizer.fit(data_standardized)

visualizer.show()
''')

st.image('assets\metodo_silhueta_6.png')