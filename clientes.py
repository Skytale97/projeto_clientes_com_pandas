import pandas as pd 

def cidade_mais_frequente(df):
    """
    Identifica a cidade que mais aparece no DataFrame.
    
    Retorna o nome da cidade (str) ou uma mensagem de erro.
    """
    if 'Cidade' in df.columns:
        contagem = df['Cidade'].value_counts()
        cidade_principal = contagem.idxmax()
        return cidade_principal
    return "Coluna 'Cidade' não encontrada"
    
def filtrar_clientes(df):
        """
    Categoriza os clientes em três faixas de renda sem deixar lacunas.
    
    Retorna três DataFrames: (altas, medias, baixas)
    """
        rendas_altas = df[df['Renda'] >= 5000.0]
        rendas_medias = df[df['Renda'].between(2000.0, 4999.0)]
        rendas_baixas = df[df['Renda'] < 2000.0]
        return rendas_altas, rendas_medias, rendas_baixas

try:
    df = pd.read_csv('dados_salvos.csv', encoding='utf-8-sig', sep=';', thousands='.')  #lê o arquivo csv com o alfabeto latino e define o ponto e vírgula como caractere de separação, e o ponto como separador de milhares;
    df.columns = df.columns.str.strip() #remove espaços em branco dos nomes das colunas, caso estes existam;
    df['Nome'] = df['Nome'].astype(str).str.strip() # remove espaços em branco dos nomes dos cliente, caso estes existam, e converte a coluna para string;
    df['Idade'] = df['Idade'].astype(int)
    df['Renda'] = df['Renda'].astype(str).str.strip().str.replace('.', '', regex=False)
    df['Renda'] = pd.to_numeric(df['Renda'], errors='coerce')  #converte o dataframe "Idade" para "int" e o dataframe "Renda" para "float", e remove os pontos que separam os milhares, caso estes existam;

    df['Media'] = df[['Idade', 'Renda']].mean(axis=1)  #gera a coluna de média entre a idade e renda;

    print("Sucesso ao ler como CSV!")  #Imprime no Terminal a Tabela;
    print("-" * 30)
    print(df)
    print("-" * 30)
    print(f"A cidade mais frequente é {cidade_mais_frequente(df)}")
    print("-" * 30)

    altas, medias, baixas = filtrar_clientes(df)
    print("Cliente(s) com renda alta (>= 5000.0):")
    print(altas[['Nome', 'Renda']] if not altas.empty else "Nenhum")
    print("-" * 40)

    print("Cliente(s) com renda média (2000.0 - 4999.0):")
    print(medias[['Nome', 'Renda']] if not medias.empty else "Nenhum")
    print("-" * 40)  
    
    print("Cliente(s) com renda baixa (< 2000.0):")
    print(baixas[['Nome', 'Renda']] if not baixas.empty else "Nenhum")

except FileNotFoundError:
    print('Arquivo não encontrado, verifique o nome e tente novamente')
except Exception as e:
    print(f'Erro ao ler o arquivo: {e}')

