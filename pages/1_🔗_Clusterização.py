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