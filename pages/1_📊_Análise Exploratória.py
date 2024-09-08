import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def build_page():
    build_header()
    build_body()

def build_header():
    text = '<h1>Análises Exploratórias</h1>' + \
           'Utilizando a base de dados fornecida pelo Centro Animal de Austin, foram criados alguns gráficos para explorar diferentes aspectos dos animais atendidos pelo abrigo.'
    st.write(text, unsafe_allow_html=True)

def read_ACC_df() -> pd.DataFrame:
    df = pd.read_csv('data/aac_intakes_outcomes.csv')
    df['age_upon_intake_(years)'] = pd.to_numeric(df['age_upon_intake_(years)'], errors='coerce')
    df['outcome_datetime'] = pd.to_datetime(df['outcome_datetime'], errors='coerce')
    translation_dict_animal = {
        'Dog': 'Cachorro',
        'Cat': 'Gato',
        'Bird': 'Pássaro',
        'Other': 'Outro'
    }
    translation_dict_condition = {
        'Normal': 'Normal',
        'Injured': 'Ferido',
        'Aged': 'Idoso',
        'Sick': 'Doente',
        'Other': 'Outro',
        'Feral': 'Selvagem',
        'Pregnant': 'Grávida',
        'Nursing': 'Amamentando'
    }
    translation_dict_intake_type = {
        'Stray': 'Abandonado',
        'Public Assist': 'Assistência Pública',
        'Owner Surrender': 'Entrega pelo Dono',
        'Euthanasia Request': 'Solicitação de Eutanásia',
        'Wildlife': 'Vida Selvagem'
    }
    df['animal_type'] = df['animal_type'].map(translation_dict_animal)
    df['intake_condition'] = df['intake_condition'].map(translation_dict_condition)
    df['intake_type'] = df['intake_type'].map(translation_dict_intake_type)
    return df

def plot_age_animal_type(df):
    df_filtered = df.dropna(subset=['age_upon_intake_(years)'])
    fig = px.bar(
        df_filtered.groupby('animal_type')['age_upon_intake_(years)'].mean().reset_index(),
        x='animal_type',
        y='age_upon_intake_(years)',
        labels={'animal_type': 'Tipo de Animal', 'age_upon_intake_(years)': 'Idade Média na Entrada (Anos)'},
        title='Idade Média na Entrada por Tipo de Animal'
    )
    st.plotly_chart(fig)

def plot_age_by_intake_condition(df):
    df_filtered = df.dropna(subset=['age_upon_intake_(years)'])
    fig = px.bar(
        df_filtered.groupby('intake_condition')['age_upon_intake_(years)'].mean().reset_index(),
        x='intake_condition',
        y='age_upon_intake_(years)',
        labels={'intake_condition': 'Condição na Entrada', 'age_upon_intake_(years)': 'Idade Média (Anos)'},
        title='Idade Média por Condição na Entrada'
    )
    st.plotly_chart(fig)

def plot_boxplot_age_animal_type(df):
    df_filtered = df.dropna(subset=['age_upon_intake_(years)'])
    fig = px.box(
        df_filtered,
        x='animal_type',
        y='age_upon_intake_(years)',
        labels={'animal_type': 'Tipo de Animal', 'age_upon_intake_(years)': 'Idade (Anos)'},
        title='Distribuição de Idade por Tipo de Animal'
    )
    st.plotly_chart(fig)

def plot_count_intake_type(df):
    intake_counts = df['intake_type'].value_counts().reset_index()
    intake_counts.columns = ['intake_type', 'count']
    fig = px.bar(
        intake_counts,
        x='intake_type',
        y='count',
        labels={'intake_type': 'Tipo de Entrada', 'count': 'Quantidade de Entradas'},
        title='Quantidade de Entradas por Tipo - Todos os Animais',
    )
    st.plotly_chart(fig)

def plot_top_breeds(df):
    breed_counts = df.groupby('breed')['count'].sum().reset_index().sort_values(by='count', ascending=False)
    top_breeds = breed_counts.head(40)
    fig = px.bar(
        top_breeds,
        x='count',
        y='breed',
        orientation='h',
        labels={'count': 'Contagem', 'breed': 'Raça'},
        title='Top Raças de Animais',
        height=800
    )
    st.plotly_chart(fig)

def build_body():
    df = read_ACC_df()
    filter_choice = st.selectbox('Selecione um Filtro Geral', ['Tipo de Animal', 'Tipo de Entrada', 'Condição de Entrada'])
    if filter_choice == 'Tipo de Animal':
        animal_choice = st.selectbox('Selecione o Tipo de Animal', df['animal_type'].unique())
        df_filtered = df[df['animal_type'] == animal_choice]
    elif filter_choice == 'Tipo de Entrada':
        intake_choice = st.selectbox('Selecione o Tipo de Entrada', df['intake_type'].unique())
        df_filtered = df[df['intake_type'] == intake_choice]
    elif filter_choice == 'Condição de Entrada':
        condition_choice = st.selectbox('Selecione a Condição de Entrada', df['intake_condition'].unique())
        df_filtered = df[df['intake_condition'] == condition_choice]
    plot_age_animal_type(df_filtered)
    plot_age_by_intake_condition(df_filtered)
    plot_boxplot_age_animal_type(df_filtered)
    plot_count_intake_type(df_filtered)
    plot_top_breeds(df)

build_page()