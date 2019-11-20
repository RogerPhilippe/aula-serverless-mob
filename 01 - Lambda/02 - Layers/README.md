# Aula 01.2 - Lambda Layers



 1. Iniciar o repositório de trabalho `sls create --template "aws-python3"`![img/slscreate.png](img/slscreate.png)
 2. Crie um arquivo chamado requirements.txt com o conteúdo 'boto3'
 3. Crie uma pasta chamada `layer`
 4. Execute o comando `pip3 install -r requirements.txt -t layer`
 5. No arquivo handler.py, deixe o topo do arquivo como na imagem. 
 ![img/topoarquivopython.png](img/topoarquivopython.png)
 6. No serverless.yml deixe o arquivo como na imagem: 
   ![img/yamllayers.png](img/yamllayers.png)
 7. Fazer deploy da função criada `sls deploy`![img/slsdeploy.png](img/slsdeploy.png) 
 8.  Testar remotamente a função `sls invoke -f hello`
![img/slsinvoke.png](img/slsinvoke.png)
 9. destrua a função feita `sls remove`



