import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Carregar o arquivo Parquet no DataFrame
data_cleaned = pd.read_parquet('data_cleaned.parquet')

# Especificar as colunas que precisam ser normalizadas
normalize_columns = [
    'dob_year', 
    'age_upon_intake_(days)',
    'age_upon_intake_(years)',
    'intake_month', 
    'intake_year',  
    'intake_number', 
    'age_upon_outcome_(days)',
    'age_upon_outcome_(years)',
    'outcome_month',
    'outcome_year',
    'outcome_number', 
    'time_in_shelter_days', 
]

# Instanciar o MinMaxScaler
min_max_scaler = MinMaxScaler()

# Criar uma cópia do DataFrame para adicionar as colunas normalizadas
data_normalized = data_cleaned.copy()

# Aplicar a normalização e adicionar as colunas normalizadas ao DataFrame
for column in normalize_columns:
    data_normalized[f'{column}_minmax'] = min_max_scaler.fit_transform(data_cleaned[[column]])

# Exibir as primeiras linhas do DataFrame normalizado para verificação
print("Primeiras linhas dos dados normalizados:")
print(data_normalized.head())

# Salvar o DataFrame normalizado em um novo arquivo Parquet
data_normalized.to_parquet('data_normalized.parquet', index=False)

print("Os dados normalizados foram salvos como 'data_normalized.parquet'.")
