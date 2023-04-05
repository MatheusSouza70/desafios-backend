<div id="top" align='center'>
 
</div>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h2 align="center">Desafios de Back-end</h2>
  <p align="center">
    Repositório do desafio back-end
    <br />
 
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Sumário</summary>
  <ol>
    <li>
      <a href="#sobre-o-desafio">Sobre o projeto</a>
      <ul>
        <li><a href="#ferramentas">Ferramentas</a></li>
        <li><a href="#requisitos">Requisitos</a></li>
        <li><a href="#funcionalidades">Funcionalidades</a></li>
      </ul>
    </li>
    <li>
      <a href="#começando-no-projeto">Começando</a>
      <ul>
        <li><a href="#pré-requisitos">Pré-requisitos</a></li>
        <li><a href="#instalação">Instalação</a></li>
      </ul>
    </li>
  </ol>
</details>


## Sobre os Desafios

<h3> Desafio 1</h3>
Este desafio consiste em criar um programa de linha de comando que lê um arquivo csv de filmes e popula um banco de dados.

<h3> Desafio 2</h3>
Este desafio consiste em criar uma documentação a partir de um código fornecido. O código em questão contém uma classe com métodos e atributos que precisam ser explicados. Sendo assim, a tarefa consiste em descrever o que cada método faz e como eles funcionam.

### Requisitos

<h3> Desafio 1</h3>

1. Cada linha do csv contém colunas que deverm ser salvas em colunas/campos separados no banco de dados;
2. ID - número inteiro que identifica o filme encontrado;
3. Title - título do filme encontrado na 2ª coluna do csv. Com o valor "Jumanji (1995)" o title é Jumanji;
4. Year - ano do filme encontrado na 2ª coluna do csv. Com o valor "Jumanji (1995)" o year é 1995;
5. Genres - múltiplos valores com os gêneros do filme separados por |. Encontrado na 3ª coluna. O script deve pensar em performance e tirar proveito de concorrência/paralelismo para popular o banco de dados.

<h3> Desafio 2</h3>

1. A documentação não tem padrão, sinta livre para escrever do jeito que você achar melhor, mas lembre que outra pessoa terá que entender.
2. Explicar de maneira clara e concisa o que pode ser feito.
3. Certificar-se de que cada método e atributo da classe sejam devidamente documentados.
4. Fornecer exemplos de uso sempre que possível, para ilustrar como cada método pode ser utilizado na prática.
5. Verificar se todas as informações fornecidas são relevantes e úteis para o usuário final.
6. Refatore o código para melhor legibilidade do mesmo.

### Ferramentas

* [Python](https://www.python.org)
* [SQLite3](https://sqlite.org/index.html)
* [PIP](https://pip.pypa.io/en/stable/installation/)
* [DB Browser (SQLite)](https://sqlitebrowser.org)


<p align="right">(<a href="#top">Voltar para o início</a>)</p>

### Funcionalidades

* [Envio de informações de um arquivo CSV para um banco de dados]()


<!-- GETTING STARTED -->
## Começando no projeto
Um pequeno exemplo de como iniciar nosso projeto.

### Pré-requisitos

* sqlite3
  ```sh
  pip install sqlite3
  ```

  
### Instalação

1. Baixe o projeto.
2. Abra o projeto em seu editor de código-fonte desejável.
3. Após aberto, você deverá abrir o terminal em seu editor de código e baixar os pré-requisitos.
4. Abra o DB Browser for SQLite e crie um banco de dados. Lembre-se do nome dele.
5. Após o banco ser criado, substitua o nome do banco de dados na variável "conn". Ele deve se parecer com "filmes.db".
6. Execute o comando com o arquivo CSV "movie.csv" em sua variável "with open", ele é o arquivo formatado que contém todos os dados.
7. Agora seu banco de dados está populado!



<p align="right">(<a href="#top">Voltar para o início</a>)</p>


