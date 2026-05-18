import pandas as pd  #importa a biblioteca pandas
try:
    df = pd.read_csv('dados_salvos.csv', encoding='latin-1', sep=';') #lê o arquivo csv com o alfabeto latino e define o ponto e vírgula como caractere de separação;
    df['Idade'] = df['Idade'].astype(int) 
    df['Renda'] = df['Renda'].astype(str).str.replace('.', '').astype(float) #converte os data frames "Idade" e "Renda" para "int" e "float", respectivamente;

    df['Media'] = df[['Idade', 'Renda']].mean(axis=1) #gera a coluna de média entre a idade e renda;

    def cidade_mais_frequente(df): #Cria a função que indica a cidade mais frequente;
        contagem = df['Cidade'].value_counts()
        cidade_principal = contagem.idxmax()
        return cidade_principal
    
    def filtrar_clientes(df): #Cria a função que  filtra os clientes - parte ainda em progesso;
        rendas_altas = df[df['Renda'] >= 5000]
        rendas_medias = df[df['Renda'].between(2000, 3500)]
        rendas_baixas =df[df['Renda'] <= 2000]
        return rendas_altas, rendas_medias, rendas_baixas

    print("Sucesso ao ler como CSV!") #Imprime no Terminal a Tabela;
    print("-" * 30)
    print(df)
    print("-" * 30)
    print(f"A cidade mais freqeunte é {cidade_mais_frequente(df)}")
    print("-" * 30)
    rendas_altas, rendas_medias, rendas_baixas = filtrar_clientes(df) 
    for nome in rendas_altas['Nome']:
        print(f"  - {nome}")    
    print("\n Pessoas com Renda Média:")
    for nome in rendas_medias['Nome']:
        print(f"  - {nome}")
    print("\n Pessoas com Renda Baixa:")
    for nome in rendas_baixas['Nome']:
        print(f"  - {nome}")
except Exception as e:
    print(f'Erro ao ler o arquivo, tente novamente')
