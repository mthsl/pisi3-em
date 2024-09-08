import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="PISI3 - EM",
    layout="wide"
)

def build_page():
    build_header()
    dicionario()

def build_header():
    text ='<h1>PISI3 - Estom e Matheus</h1>' + \
       '<p>Este projeto visa realizar análises utilizando os dados disponibilizados pelo Centro Animal de Austin. '+ \
       'Os dados foram obtidos a partir do conjunto de dados disponível no ' + \
       '<a href="https://www.kaggle.com/datasets/aaronschlegel/austin-animal-center-shelter-intakes-and-outcomes?select=aac_intakes_outcomes.csv" target="_blank">Kaggle</a>.</p>'
    st.write(text, unsafe_allow_html=True)

def dicionario():
    with st.expander('Dicionário de Dados'):
        st.write('''<table>
            <tr><th>Coluna</th><th>Descrição</th></tr>
            <tr><td>age_upon_outcome</td><td>A idade do animal no momento da saída</td></tr>
            <tr><td>animal_id_outcome</td><td>O ID da saída do animal. Deve corresponder à coluna de ID de entrada</td></tr>
            <tr><td>date_of_birth</td><td>Data de nascimento do animal. Estimada se a data exata de nascimento não for conhecida</td></tr>
            <tr><td>outcome_subtype</td><td>Tipo de saída mais específico correspondente ao tipo de saída, onde apropriado</td></tr>
            <tr><td>outcome_type</td><td>O tipo de saída</td></tr>
            <tr><td>sex_upon_outcome</td><td>O gênero do animal e se ele foi castrado ou esterilizado no momento da saída</td></tr>
            <tr><td>age_upon_outcome_(days)</td><td>A idade do animal no momento da saída representada em dias</td></tr>
            <tr><td>age_upon_outcome_(years)</td><td>A idade do animal no momento da saída representada em anos</td></tr>
            <tr><td>age_upon_outcome_age_group</td><td>Agrupamentos de faixas etárias do animal no momento da saída. Incrementos de 2,5 anos</td></tr>
            <tr><td>outcome_datetime</td><td>Data e hora em que a saída ocorreu</td></tr>
            <tr><td>outcome_month</td><td>O mês representado como um valor numérico de 1 a 12 em que a saída ocorreu</td></tr>
            <tr><td>outcome_year</td><td>O ano da saída</td></tr>
            <tr><td>outcome_monthyear</td><td>Mês e ano da saída representados como data e hora</td></tr>
            <tr><td>outcome_weekday</td><td>Dia da semana em que a saída ocorreu</td></tr>
            <tr><td>outcome_hour</td><td>Hora da saída representada como um valor numérico de 1 a 24</td></tr>
            <tr><td>outcome_number</td><td>Valor numérico indicando se um animal foi liberado do abrigo mais de uma vez. Valores superiores a 1 indicam que o animal foi levado ao abrigo e saiu mais de uma vez</td></tr>
            <tr><td>dob_year</td><td>Ano de nascimento do animal</td></tr>
            <tr><td>dob_month</td><td>Mês de nascimento do animal representado como número</td></tr>
            <tr><td>dob_monthyear</td><td>Data e hora da data de nascimento</td></tr>
            <tr><td>age_upon_intake</td><td>A idade do animal no momento da entrada</td></tr>
            <tr><td>animal_id_intake</td><td>O ID único dado ao animal no momento da entrada. Deve corresponder ao ID de saída do animal</td></tr>
            <tr><td>animal_type</td><td>Tipo de animal. Pode ser 'gato', 'cachorro', 'pássaro', etc.</td></tr>
            <tr><td>breed</td><td>Raça do animal</td></tr>
            <tr><td>color</td><td>Cor do animal</td></tr>
            <tr><td>found_location</td><td>Endereço ou área geral onde o animal foi encontrado</td></tr>
            <tr><td>intake_condition</td><td>A condição de entrada do animal. Pode ser 'normal', 'ferido', 'doente', etc.</td></tr>
            <tr><td>intake_type</td><td>O tipo de entrada, por exemplo, 'animal de rua', 'entrega pelo dono', etc.</td></tr>
            <tr><td>sex_upon_intake</td><td>O gênero do animal e se ele foi castrado ou esterilizado no momento da entrada</td></tr>
            <tr><td>count</td><td>Coluna auxiliar para tabulação de contagens. Todas as linhas desta coluna são 1</td></tr>
            <tr><td>age_upon_intake_(days)</td><td>A idade do animal no momento da entrada representada em dias</td></tr>
            <tr><td>age_upon_intake_(years)</td><td>A idade do animal no momento da entrada representada em anos</td></tr>
            <tr><td>age_upon_intake_age_group</td><td>Grupo etário do animal no momento da entrada. Grupos em incrementos de 2,5 anos</td></tr>
            <tr><td>intake_datetime</td><td>Data e hora em que a entrada ocorreu</td></tr>
            <tr><td>intake_month</td><td>Mês numérico em que a entrada ocorreu</td></tr>
            <tr><td>intake_year</td><td>Ano da entrada</td></tr>
            <tr><td>intake_monthyear</td><td>Mês e ano da entrada como data e hora</td></tr>
            <tr><td>intake_weekday</td><td>O dia da semana em que a entrada ocorreu</td></tr>
            <tr><td>intake_hour</td><td>Hora representada como valor de 1 a 24, indicando a hora em que a entrada ocorreu</td></tr>
            <tr><td>intake_number</td><td>O número de entrada indicando o número de vezes que o animal foi levado ao abrigo. Valores superiores a 1 indicam que o animal foi levado ao abrigo mais de uma vez</td></tr>
            <tr><td>time_in_shelter</td><td>O tempo no abrigo originalmente representado como um objeto TimeDelta</td></tr>
            <tr><td>time_in_shelter_days</td><td>Valor numérico indicando o número de dias que o animal permaneceu no abrigo, desde a entrada até a saída</td></tr>
        </table>
        <br>
''', unsafe_allow_html=True)


build_page()