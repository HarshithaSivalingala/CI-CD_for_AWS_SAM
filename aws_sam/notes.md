* Make sure you have AWS SAM CLI installed on your machine (MAC):
* $`brew install aws/tap/aws-sam-cli`
* To build $`sam build --debug` or `sam build`
* To deploy $`sam deploy --guided`
* Validate SAM template: $`sam validate`
* Invoke Function locally: $`sam local invoke` (you need to have Docker installed and running).
* To Invoke the function locally and pass payload to the local run: $`sam local invoke ContactFormFunction --event lambda/tests/event.json`