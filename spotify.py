import requests
import json

######## FAZENDO A REQUISIÇÃO GET PARA A API DO SPOTIFY
# Definindo o header com o token de autorização
headers = {"Authorization" : "Bearer BQAorcPlNAQ1M2mYmGpafEtLFj-vUs-G1Rfy4wbpUcxnWc9_MJs6ekt0KtXLsfsx5rw-9AXS_hWIZc5Bz8PT7fxpScloJ2-qQIzcY1mteQ3XQ8oCih6h"}

#Cria uma dicionário com os IDs fornecidos para a requisição
artistas = {
    "Ed Sheeran" : "6eUKZXaKkcviH0Ku9w2n3V",
    "Queen": "1dfeR4HaWDbWqFHLkxsg1d",
    "Ariana Grande" : "66CXWjxzNUsdJxJ2JdwvnR",
    "Maroon 5" : "04gDigrS5kc9YWfZHwBETP",
    "Imagine Dragons" : "53XhwfbYqKCa1cC15pYq2q",
    "Eminem": "7dGJo4pcD2V6oG8kP0tJRR",
    "Lady Gaga" : "1HY2Jd0NmPuamShAr6KMms",
    "Cold Play" : "4gzpq5DPGxSnKTe4SA8HAU",
    "Beyonce" : "6vWDO969PvNqNYHIOW5v0m",
    "Bruno Mars" : "0du5cEVh5yTK9QJze8zA0C",
    "Rihanna" : "5pKCCKE2ajJHZ9KAiaK11H",
    "Shakira" : "0EmeFodog0BfCgMzAIvKQp",
    "Justin Bieber" : "1uNFoZAHBGtllmzznpCI3s",
    "Demi Lovato" : "6S2OmqARrzebs0tKUEyXyp",
    "Taylor Swift" : "06HL4z0CvFAxyc27GXpf02"
}

# Extraindo os IDs
ids = list(artistas.values())

# Endoint para a requisição da API
endpoint_spotify= "https://api.spotify.com/v1/artists?ids=" + ",".join(ids)

# Efetua a requisição get
pedido = requests.get(endpoint_spotify, headers=headers)

# Verifica se a requisição tem sucesso
if (pedido.status_code == 200):
    infos_artista = json.loads(pedido.text)
    # print(infos_artista)
else:
    print("Falha na requisição")

##### TRATAMENTO DOS DADOS 
# Mantém somente a lista de dicionários que contém as informações dos artistas especificados
my_list = infos_artista["artists"]

# Lista que receberá as informações tratadas
lista_tratada = []


i = 0
size = len(my_list)
while (i < size): ## Enquanto a lista não acabar, recebe as informações dos artistas e guarda em um dicionário organizado, somente com as informações necessárias.
        temp = {}
        temp['artist_name'] = my_list[i]['name']
        temp['followers'] = my_list[i]['followers']['total']
        temp['popularity'] = my_list[i]['popularity']
        lista_tratada.append(temp)
        i += 1

# Organizando a lista de artistas com mais seguidores
follower_ranking_all = sorted(lista_tratada, key=lambda x: x['followers'], reverse=True)
# Formatando para a impressão solicitada
follower_ranking = [{'artist_name': f['artist_name'], 'followers':f['followers']} for f in follower_ranking_all]

# Organizando a lista de artistas com maior índice de popularidade
popularity_ranking_all = sorted(lista_tratada, key=lambda x: x['popularity'], reverse=True)
# Formatando para a impressão solicitada
popularity_ranking = [{'artist_name' : f['artist_name'], 'popularity' : f['popularity']} for f in popularity_ranking_all]