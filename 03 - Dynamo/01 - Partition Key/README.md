# 03.1 - Partition key


1. No terminal do IDE criado no cloud9 execute o comando `cd ~/environment/aula-serverless-mob/03\ -\ Dynamo/01\ -\ Partition\ Key/` para entrar na pasta que fara este exercicio.
2. Em uma nova aba abra o console da AWS e vá para o serviço DynamoDB.
3. Clique em Criar Tabela no painel do dynamoDB
![img/partitionkey01.png](img/partitionkey01.png)
4. Preencha os dados como na imagem e clique em Criar
![img/partitionkey02.png](img/partitionkey02.png)
5. A tabela pode levar alguns minutos para ser criada
6. Modifique o arquivo 'dynamo.py' utilizando o IDE para que fique como na imagem
![img/partitionkey03.png](img/partitionkey03.png)
7. Para executar o arquivo basta via linha de comando ir até a pasta onde ele se encontra e rodar o comando `python3 dynamo.py`
8. Se voltar a pagina do dynamoDB e atualizar verá que temos apenas um registro. Isso ocorreu porque quando inserirmos partition keys identicas o banco sobrescreve o registro anterior.
![img/partitionkey04.png](img/partitionkey04.png)
9. Altere o arquivo 'dynamo.py' para que as partition keys fiquem diferentes
![img/partitionkey05.png](img/partitionkey05.png)
10. execute novamente o arquivo `python3 dynamo.py`
11. Agora a tabela book tem 3 registros, cada um com seu atributo
![img/partitionkey06.png](img/partitionkey06.png)