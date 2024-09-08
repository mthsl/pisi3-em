import pandas as pd

# Defina o caminho para o arquivo .csv no seu sistema local
csv_file_name = 'aac_intakes_outcomes.csv'

# Carregue o arquivo .csv no pandas
data = pd.read_csv(csv_file_name)

# Exiba as primeiras linhas do DataFrame para verificar o carregamento
print("Primeiras linhas dos dados:")
print(data.head())

# Exiba informações gerais sobre o DataFrame para verificar tipos de dados e valores ausentes
print("\nInformações gerais dos dados:")
print(data.info())

# Defina o nome do arquivo Parquet
parquet_file_name = csv_file_name.replace('.csv', '.parquet')

# Salve o DataFrame como um arquivo Parquet
data.to_parquet(parquet_file_name, index=False)

print(f"Arquivo CSV foi convertido e salvo como {parquet_file_name}")