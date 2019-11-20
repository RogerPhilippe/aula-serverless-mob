# 03.3 - Local Secondary Key

1. No terminal do IDE criado no cloud9 execute o comando `cd ~/environment/aula-serverless-mob/03\ -\ Dynamo/03\ -\ Local\ Secondary\ Key/` para entrar na pasta que fara este exercicio.
2. Em uma nova aba abra o console da AWS e vá para o serviço DynamoDB.
3. Clique em 'Criar Tabela'e preencha o formulário como na imagem, após desabilite a opção 'Usar configurações padrão' e clique em 'Adicionar indice'
![img/localsecondaryindex01.png](img/localsecondaryindex01.png)
4. Preencha o popup que abriu como na imagem e clique em 'Adicionar Índice':
   ![img/localsecondaryindex01-2.png](img/localsecondaryindex02.png)
5. Desmarque as opções de Auto Scalling e deixe o 'Capacidade provisionada' como na imagem, e clique em 'Criar'
![alt](img/localsecondaryindex03.png)
6. Altere o arquivo 'dynamo.py' para inserir registros na tabela criada como na imagem
![img/localsecondaryindex04.png](img/localsecondaryindex04.png) 
7. Execute o arquivo com o comando `python3 dynamo.py` no terminal
![alt](img/localsecondaryindex05.png)
8. Escolha um usuario e um range de um segundo para executar o arquivo 'dynamo.py' como no exemplo
![img/localsecondaryindex06.png](img/localsecondaryindex06.png)
9. execute o comando `python3 dynamo.db`
10. Escolha uma store e altere o arquivo 'dynamo.py'
![img/localsecondaryindex07.png](img/localsecondaryindex07.png)
11. Execute o comando `python3 dynamo.py`
    