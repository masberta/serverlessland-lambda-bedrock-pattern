import json
import boto3

bedrock_runtime = boto3.client('bedrock-runtime')

def handler(event, context):
    request_word = event['word']

    request_context = event['context']
    request_string = "definition of "+request_word + \
        " in this context:"+request_context
    request_body = {
        "prompt": request_string,
        "temperature": 0.5,
        "topP": 0.5,
        "maxTokens": 200,
        "stopSequences": [],
        "countPenalty": {
            "scale": 0
        },
        "presencePenalty": {
            "scale": 0
        },
        "frequencyPenalty": {
            "scale": 0
        }
    }

    body = bedrock_runtime.invoke_model(body=json.dumps(request_body),
    modelId="ai21.j2-mid")['body'].read().decode('utf-8')
    body = json.loads(body)

    return {
        'statusCode': 200,
        'body': json.dumps(body["completions"][0]["data"]["text"])
    }
