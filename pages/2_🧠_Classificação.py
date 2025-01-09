# Importando as bibliotecas necessárias
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pickle
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Função para carregar modelos e dados do arquivo pickle
@st.cache_data
def carregar_modelos_dados(file_path):
    with open(file_path, 'rb') as file:
        return pickle.load(file)

# Função para exibir resultados do modelo
def exibir_resultados(modelo, nome_modelo, x_test, y_test, classes):
    y_pred = modelo.predict(x_test)
    
    # Relatório de classificação
    st.markdown(f"### Relatório de Classificação - {nome_modelo}")
    st.text(classification_report(y_test, y_pred, target_names=classes))
    
    # Matriz de confusão
    cm = confusion_matrix(y_test, y_pred)
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=classes, yticklabels=classes)
    ax.set_title(f'{nome_modelo} - Matriz de Confusão')
    ax.set_xlabel('Classe Prevista')
    ax.set_ylabel('Classe Verdadeira')
    st.pyplot(fig)
    
    # Acurácia
    acuracia = accuracy_score(y_test, y_pred)
    st.markdown(f"**Acurácia - {nome_modelo}:** {acuracia:.4f}")
    return acuracia

# Função para exibir os resultados da validação cruzada
def exibir_validacao_cruzada_mockada():
    st.markdown("### Resultados da Validação Cruzada Mockada")
    validacao_mockada = {
        "Random Forest": {
            "folds": [0.8164233576642336, 0.814051094890511, 0.8166058394160584, 0.8170924574209246, 0.8165450121654502],
            "media": 0.8109,
            "desvio": 0.0010
        },
        "Decision Tree": {
            "folds": [0.7810827250608272, 0.7855231143552311, 0.7860705596107056, 0.7774330900243309, 0.777250608272506],
            "media": 0.7805,
            "desvio": 0.0031
        },
        "XGBoost": {
            "folds": [0.8100973236009732, 0.8130778588807785, 0.815632603406326, 0.8112530413625304, 0.8094282238442823],
            "media": 0.8108,
            "desvio": 0.011
        }
    }

    for modelo, valores in validacao_mockada.items():
        st.markdown(f"**Modelo: {modelo}**")
        st.markdown(f"Acurácias em cada fold: {valores['folds']}")
        st.markdown(f"Acurácia Média: {valores['media']:.4f}")
        st.markdown(f"Desvio Padrão: {valores['desvio']:.4f}")
        st.markdown("---")

# Função para exibir SHAP plots via imagem
def exibir_shap_imagem():
    st.markdown("### Importância das Features (SHAP)")
    st.image('assets/SHAP_modelo_xgboost.png', caption="Importância das Features (SHAP) - XGBoost", use_column_width=True)

# Função principal do Streamlit
def main():
    st.title("📊 Análise de Modelos de Classificação")
    
    # Input para o caminho do arquivo pickle
    file_path = 'data/modelos_treinados (3).pkl'
    
    try:
        # Carregar os modelos e os dados ao iniciar a aplicação
        st.markdown("Carregando os modelos e dados do arquivo...")
        modelos_dados_carregados = carregar_modelos_dados(file_path)
        
        # Extrair os modelos, dados de teste e classes
        model_rf = modelos_dados_carregados['RandomForest']
        model_dt = modelos_dados_carregados['DecisionTree']
        model_xgb = modelos_dados_carregados['XGBoost']
        x_test = modelos_dados_carregados['x_test']
        y_test = modelos_dados_carregados['y_test']
        classes = ['Não Adotado', 'Adotado', 'Morto']
        
        # Filtros para selecionar o que visualizar
        st.sidebar.title("Filtros")
        opcao_visualizacao = st.sidebar.radio(
            "Selecione o que deseja visualizar",
            ("Random Forest", "Decision Tree", "XGBoost", "Validação Cruzada", "SHAP")
        )
        
        # Exibir resultados com base no filtro
        if opcao_visualizacao == "Random Forest":
            st.markdown("## Resultados - Random Forest")
            exibir_resultados(model_rf, "Random Forest", x_test, y_test, classes)
        elif opcao_visualizacao == "Decision Tree":
            st.markdown("## Resultados - Decision Tree")
            exibir_resultados(model_dt, "Decision Tree", x_test, y_test, classes)
        elif opcao_visualizacao == "XGBoost":
            st.markdown("## Resultados - XGBoost")
            exibir_resultados(model_xgb, "XGBoost", x_test, y_test, classes)
        elif opcao_visualizacao == "Validação Cruzada":
            exibir_validacao_cruzada_mockada()
        elif opcao_visualizacao == "SHAP":
            exibir_shap_imagem()
    
    except Exception as e:
        st.error(f"Erro ao carregar os dados: {e}")

if __name__ == "__main__":
    main()
