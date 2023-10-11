# serverlessland-lambda-bedrock-pattern



## Getting started

This code sample allows you to infere any foundational models enabled in Bedrock by passing an event payload to a Lamdba function. The payload must contain `model_id` and `request_body`

The model id and request body payload examples can be found in the AWS Console, this repository provide four payload examples for `Jurassic-2 Mid` and `ClaudeV2`

Bedrock models must be enabled in the AWS Console to be infered.

## Deployment

Exeute the below steps on a terminal with [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) and [AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html), it's strongly suggested to leverage an Amazon Linux [Cloud9](https://docs.aws.amazon.com/cloud9/latest/user-guide/create-environment-main.html) environment.

### Get into CDK directory stack:

`cd lambda-layer`

### If deploying in an account with CDK for the first time:

`cdk bootstrap`

### To deploy:

`cdk deploy`

## Test your function

Verify deployment in the AWS Console and copy function name.

`cd tests`

Grant execution permissions to the `test.sh` script:

`sudo chmod +x test.sh`

Invoke the script with the following parameters:
- `-f [FunctionName]`
- `-m [model]`
- `-e [event]`

Four example payloads are provided for `ClaudeV2` (/tests/events/claude) and `Jurassic-2 Mid` (/test/events/ai21) with the following prompt:

1. "Define 'function' in this context:A Javascript function can be ran asynchronously"
2. "Define 'function' in this context:the promotion required more responsibilities in his job function"
3. "Define 'function' in this context:the engine ran out of fuel and stopped to function"
4. "Define 'function' in this context:the math teacher wrote a function on the blackboard"

Inoke the Lamdba function by passing a numeric value for the event i.e. `-e 1` and desired model, i.e. `-m ai21` and function name, i.e. `-f LambdaLayerStack-LambdaFunctionBF21E41F-XzRF7ZvYq6Kj`

## Invocation example

Lets invoke `Jurassic-2 Mid` with the first event payload:

`./test.sh -f LambdaLayerStack-LambdaFunctionBF21E41F-XzRF7ZvYq6Kj -m ai21 -e 1`

The file `ai21-event1.json` will be created with the response.

A successful response will return:

```
{"statusCode": 200, "model_id": "ai21.j2-mid-v1", "execution_time": [execution time in ms], "body": "[model repsonse]"
```

If an error occures it will return:

```
{"statusCode": 500, "request_body": "[request_body event payload]", "models": "[list of foundational models enabled in Bedrock]"
```


