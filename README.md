# Desafio-tecnico-engenharia-de-dados-Sicredi

POC para criação de um Data Lake para o desafio

  ## 1) Requisitos necessários para rodar o projeto.

É necessário ter instalados na máquina o **Docker** e **Python 3**.


  ## 2) Lógica

  Como a ingesão de dados envolvia apenas dados estruturados, optei por utiizar o spark como framework de etl or ter muita familiaridade com a linguagem **Python**, o 
desenvolvimento do projeto foi feito utilizando **Spark SQL**.

  ## 3) Procedimentos para execução;

 1. Abrir o terminal/CMD na pasta raiz;
 2. Executar `docker-compose up -d` no diretório onde o arquivo **Dockerfile** se encontra;
 3. Executar `pip install -r requirements.txt`
 4. Avaliar se os serviços já estão disponíveis no contêiner;
 5. Executar `python3 runner.py {caminho_onde_salvar_csv_sem_aspas}`

Após seguir essas etapas, o script irá provisionar um cluster **Spark**, com um **Worker** , e o banco de dados MySQL, que irá ser preenchido com os dados iniciais. 
O script `runner.py` irá se conectar com o banco através do **Spark** e executar o cruzamento das tabelas em formato de **DF** para agregar em um único arquivo flat. 

