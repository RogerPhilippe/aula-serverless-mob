# Aula 02.1 - Primeira api com lambda

### Criando o lambda

1. Na pagina princial do serviço Lambda, clique em 'Create Function'
![img/create-function.png](img/create-function.png)
2. Preencha com as informações pedidas
![img/create-function-options.png](img/create-function-options.png)
3. copie o conteudo do arquivo lambda.py e cole no editor da função
![img/copying-code-to-function.png](img/copying-code-to-function.png)
4. Clique em 'Save' no topo da página

### Criando a api
1. Selecione 'new api' e coloque o nome:
![img/create-api-name.png](img/create-api-name.png)
2. Clique em 'actions' e depois em 'Create Reource'
![img/create-resource.png](img/create-resource.png)
3. Preencha o formulario e clique no botão 'Create Resource'
![img/filling-resource.png](img/filling-resource.png)
4. Clique em 'Actions' e deplois em 'Create Method' e selecione o metodo get
![img/selecting-method.png](img/selecting-method.png)
5. Preencha os parametros conforme a imagem, após clique em save
![img/api-get-parameters-lambda.png](img/api-get-parameters-lambda.png)
6. Clique em 'Actions' e selecione 'Deploy API'
7. Em 'Deployment Stage' selecione '[New Stage]', preencha o que é pedido, e clique em 'Deploy'
![img/deploy-api.png](img/deploy-api.png)
8. Para testar é só utilizar a url que foi fornecida e adcionar /helloworld no navegador
![img/using-api.png](img/using-api.png)
