import pandas as pd 
import polars as pl 
from datetime import datetime

ENDERECO_DADOS = './../DADOS/'

#pandas 24 segs
#polars 10 segs
try:
    inicio = datetime.now()
    print('Obtendo dados parquet...')


    #Scan Parquet: Cria um plano de execução. Não obtem os dados direto. 
    df_bolsa_familia = pl.scan_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet')

    #Colect: Executa o plano de execução e traz os dados 

    
    df_bolsa_familia = df_bolsa_familia.collect()
    print(df_bolsa_familia.head())

    fim = datetime.now()
    print(f'Tempo: {fim - inicio}')

except Exception as e:
    print(f'Erro ao obter dados parquet {e}')