import sys 
sys.path.insert(0,'/opt')

import boto3
import slackweb

sns = boto3.client('sns')

def lambda_handler(event, context):
    message = event['Records'][0]['Sns']['Message']
    slack = slackweb.Slack(url="https://hooks.slack.com/services/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")
    slack.notify(text=str(message),channel="#atividade-slack" username="serverless-bot", icon_emoji=":squirrel: :shitpit:")