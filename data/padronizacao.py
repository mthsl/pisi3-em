import pandas as pd
from sklearn.preprocessing import StandardScaler

# Carregar o arquivo Parquet no DataFrame
data_cleaned = pd.read_parquet('data_cleaned.parquet')

# Especificar as colunas que precisam ser padronizadas
scale_columns = [
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

# Instanciar o StandardScaler
standard_scaler = StandardScaler()

# Criar uma cópia do DataFrame para adicionar as colunas padronizadas
data_standardized = data_cleaned.copy()

# Aplicar a padronização e adicionar as colunas padronizadas ao DataFrame
for column in scale_columns:
    data_standardized[f'{column}_standardized'] = standard_scaler.fit_transform(data_cleaned[[column]])

# Exibir as primeiras linhas do DataFrame padronizado para verificação
print("Primeiras linhas dos dados padronizados:")
print(data_standardized.head())

# Salvar o DataFrame padronizado em um novo arquivo Parquet
data_standardized.to_parquet('data_standardized.parquet', index=False)

print("Os dados padronizados foram salvos como 'data_standardized.parquet'.")