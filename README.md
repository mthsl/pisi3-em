# PISI3 - EM

por: Estom Paulino e Matheus Lima.

Este projeto é utilizado para as aulas da disciplina de Projeto Interdisciplinar para Sistemas de Informação III, do 3° período do curso de Bacharelado em Sistemas de Informação da Universidade Federal Rural de Pernambuco (UFRPE).

O objetivo deste projeto é investigar e analisar os padrões e fatores que influenciam o processo de adoção de animais em abrigos.

# Passos para a instalação:
* Instale o VSCode.
* Efetue o clone do projeto: `CTRL+SHIFT+P > Git:Clone > Clone from GitHub > `
* Instale o python.
* Acesse a aba "Terminal" disponível na parte inferior do VSCode.
* Execute a linha abaixo para criar um ambiente virtual do python para o projeto. Observe que a pasta `venv` está no `.gitignore`.
    `python -m venv venv`
* Atualize o pip:
    `python -m pip install --upgrade pip`  
* Instale as libs necessárias para o projeto:
    `pip install -r requirements.txt --upgrade`
* Rode o sistema:
    `streamlit run Home.py`