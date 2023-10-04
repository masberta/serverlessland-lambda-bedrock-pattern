import json
import boto3

bedrock = boto3.client('bedrock')
bedrock_runtime = boto3.client('bedrock-runtime')
request_string="definition of screwed in this context:He firmly attched the decoration screwed to the wall"
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

body=bedrock_runtime.invoke_model(body=json.dumps(request_body), 
modelId="ai21.j2-mid")['body'].read().decode('utf-8')
body=json.loads(body)

print(type(body))
def handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps(body["completions"][0]["data"]["text"])
    }


