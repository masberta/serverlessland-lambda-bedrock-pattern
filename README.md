# serverlessland-lambda-bedrock-pattern



## Getting started

Get into CDK directory stack:

`cd lambda-layer`

If you're deploying in an account with CDK for the first time:

`cdk bootstrap`

To deploy:

`cdk deploy`

## Test your function

Verify deployment in the AWS Console and copy function name.

`cd tests`

Edit the `test` script by providing the function name to the `fn` variable

`source test`

This will execute a bash script invoking the Lambda function just deployed.
Open `response1.json` to `reponse4.json` to validate the Lambda funtion sucessfully invoked Bedrock and provided the correct definition of `function` in four different contexts.


