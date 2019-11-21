# Aula 05.3 - Lambda

1. Crie uma pasta 'lambda'
2. Copie o arquivo 'requirements.txt' que esta na raiz do módulo para dentro da pasta 'lambda'
3. Entre na pasta 'lambda' e execute o comando `pip3 install -r requirements.txt -t .`
4. Crie um arquivo 'serverless.yml' com o seguinte conteudo
![img/lambda-01.png](img/lambda-01.png)
5. Crie um arquivo 'lambda.py' com o seguinte conteudo
![img/lambda-02.png](img/lambda-02.png)
6. Na URL do slack deixe o seguinte conteudo `https://hooks.slack.com/services/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`
7. No channel coloque o seguinte `serverless-aws`
8. Execute o comando `sls deploy`
9. Agora cada vez que você publicar uma mensagem para o SNS irá receber uma mensagem no slack

