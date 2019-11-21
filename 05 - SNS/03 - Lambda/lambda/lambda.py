import boto3
import slackweb

sns = boto3.client('sns')

def lambda_handler(event, context):
    message = event['Records'][0]['Sns']['Message']
    slack = slackweb.Slack(url="https://hooks.slack.com/services/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")
    slack.notify(text=str(message),channel="#serverless-aws" username="serverless-bot", icon_emoji=":squirrel: :shitpit:")