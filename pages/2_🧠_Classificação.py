# Importando as bibliotecas necessárias
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import pickle

# Carregar os modelos e dados do arquivo pickle
def carregar_modelos_dados(file_path):
    with open(file_path, 'rb') as file:
        return pickle.load(file)

# Função para exibir a Matriz de Confusão, Acurácia e Relatório de Classificação
def exibir_resultados(modelo, nome_modelo, x_test, y_test):
    # Previsão do modelo
    y_pred = modelo.predict(x_test)

    # Exibindo a matriz de confusão
    cm = confusion_matrix(y_test, y_pred)
    fig, ax = plt.subplots()
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Não adotado', 'Adotado'], yticklabels=['Não adotado', 'Adotado'], ax=ax)
    ax.set_title(f'{nome_modelo} - Matriz de Confusão')
    ax.set_xlabel('Classe Prevista')
    ax.set_ylabel('Classe Verdadeira')
    st.pyplot(fig)

    # Exibindo o relatório de classificação
    st.markdown(f"### Relatório de Classificação - {nome_modelo}")
    st.text(classification_report(y_test, y_pred, target_names=['Não adotado', 'Adotado']))

    # Exibindo a acurácia do modelo
    acuracia = accuracy_score(y_test, y_pred)
    st.markdown(f"**Acurácia - {nome_modelo}:** {acuracia:.4f}")
    return acuracia

# Função principal do Streamlit
def main():
    st.title("📊 Classificação dos Dados")
    st.markdown("## Resultados dos Modelos de Classificação")
    
    # Carregar os modelos e os dados do arquivo .pkl
    file_path = st.text_input("Caminho do arquivo .pkl", value='data/modelos_treinados (1).pkl')
    
    if st.button("Carregar Modelos e Dados"):
        try:
            modelos_dados_carregados = carregar_modelos_dados(file_path)
            st.success("Modelos e dados carregados com sucesso!")
            
            # Carregar os modelos e os dados
            model_rf_carregado = modelos_dados_carregados['RandomForest']
            model_dt_carregado = modelos_dados_carregados['DecisionTree']
            model_gb_carregado = modelos_dados_carregados['GradientBoosting']
            x_test_carregado = modelos_dados_carregados['x_test']
            y_test_carregado = modelos_dados_carregados['y_test']

            # Exibir resultados para cada modelo
            st.markdown("## Resultados para o modelo: Random Forest")
            acuracia_rf = exibir_resultados(model_rf_carregado, "Random Forest", x_test_carregado, y_test_carregado)
            st.image('assets\\feature_importance_RF.png')
            
            st.markdown("## Resultados para o modelo: Decision Tree")
            acuracia_dt = exibir_resultados(model_dt_carregado, "Decision Tree", x_test_carregado, y_test_carregado)
            st.image('assets\\feature_importance_DT.png')

            st.markdown("## Resultados para o modelo: Gradient Boosting")
            acuracia_gb = exibir_resultados(model_gb_carregado, "Gradient Boosting", x_test_carregado, y_test_carregado)
            st.image('assets\\SHAP GB.png')
            
            # Exibindo as acurácias de cada modelo
            st.markdown("## Comparação de Acurácias")
            st.markdown(f"**Acurácia do modelo Random Forest:** {acuracia_rf:.4f}")
            st.markdown(f"**Acurácia do modelo Decision Tree:** {acuracia_dt:.4f}")
            st.markdown(f"**Acurácia do modelo Gradient Boosting:** {acuracia_gb:.4f}")

        except Exception as e:
            st.error(f"Erro ao carregar o arquivo: {str(e)}")

if __name__ == "__main__":
    main()
