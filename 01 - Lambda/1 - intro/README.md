# Aula 01 - Lambda



 1. Instalar serverless framework `npm install -g serverless`
 2. Iniciar o repositório de trabalho `sls create --template "aws-python3"`
 ![img/slscreate.png](img/slscreate.png)

 3. Fazer deploy da função crada `sls deploy`
 ![img/slsdeploy.png](img/slsdeploy.png)

 4. Testar remotamente a função `sls invoke -f hello`
![img/slsinvoke.png](img/slsinvoke.png)
 5. Altere a versão do retorno da função para 1.1
 6. Faça um teste local da sua função `sls invoke local -f hello` 
![img/slsinvokelocal.png](img/slsinvokelocal.png)
 7. destrua a função feita `sls remove`
