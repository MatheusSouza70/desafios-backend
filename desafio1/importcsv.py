import csv
import sqlite3 
#Importação das Bibliotecas

conn = sqlite3.connect('filmes.db') #Procura do nome do banco SQLITE
cursor = conn.cursor() #Firma conexão com o banco de dados

cursor.execute("DROP TABLE IF EXISTS filmes") #dropa a tabela caso ela já exista, para evitar tabelas com nomes correlatos
cursor.executescript('''CREATE TABLE filmes(
    "movieId" int(6) primary key,
    "title" VARCHAR(70),
    "year" INT(4),
    "genres" VARCHAR(40)
)'''
)#criação da tabela com os datatypes e o nome das colunas

#Comando para criação do banco de dados

with open('./data/movie.csv') as csv_file: #abre o arquivo csv e o nomeia como "csv_file"
    csv_reader = csv.reader(csv_file, delimiter=';') #utiliza a função de leitura do csv, com o delimitador ";"

    for row in csv_reader: # pra cada linha no leitor csv, o cursor irá executar o script de inserção
        cursor.execute(
            "INSERT INTO filmes (movieId, title, year, genres) VALUES (?, ?, ?, ?)", row) 
#Comando para inserção dos dados do arquivo CSV para o banco de dados

conn.commit() #commit nos comandos acima
conn.close() #Fecha a conexão com o banco
