# 03.4 - Global Secondary Key

1. No terminal do IDE criado no cloud9 execute o comando `cd ~/environment/aula-serverless-mob/03\ -\ Dynamo/04\ -\ Global\ Secondary\ Key/` para entrar na pasta que fara este exercicio.
2. Em uma nova aba abra o console da AWS e vá para o serviço DynamoDB. 
3. Dessa vez vamos criar uma tabela chamada 'sell_gsi' com as configurações da imagem abaixo:
   ![img/globalsecondarykey-0.png](img/globalsecondarykey-0.png)
4. Após a finalização de criação da tabela vá até a aba 'Indices', e clique em 'Criar Índice'.
![img/globalsecondarykey-1.png](img/globalsecondarykey-1.png)
5. Preencha como a imagem, e clique em 'Criar Índice'. Esse processo pode demorar.
![img/globalsecondarykey-2.png](img/globalsecondarykey-2.png)
6. Altere o arquivo 'dynamo.py' para que fique como na foto
![img/globalsecondarykey-3.png](img/globalsecondarykey-3.png)
7. Execute o arquivo com o comando `python3 dynamo.py`
![img/globalsecondarykey-4.png](img/globalsecondarykey-4.png)
8. Altere o arquivo 'dynamo.py' para que fique como na foto, escolhendo um invervalo valido de um segundo para o usuario pesquisado
![img/globalsecondarykey-5.png](img/globalsecondarykey-5.png)
9. Execute o arquivo com o comando `python3 dynamo.py`
10. Altere o arquivo 'dynamo.py' para que fique como na foto, escolhendo um invervalo valido de um segundo para a loja pesquisado
![img/globalsecondarykey-6.png](img/globalsecondarykey-6.png)
11. Execute o arquivo com o comando `python3 dynamo.py`
