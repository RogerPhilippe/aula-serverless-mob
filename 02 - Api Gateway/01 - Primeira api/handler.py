from json import dumps

def response(status_code, body):
    message = {
        "statusCode": status_code,
        "body": dumps(body)
    }
    return message

def lambda_handler(event, context):
    return response(200,{'hello':'world'})