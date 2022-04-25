# SAM application template
## Setup
In order to build up the Lambda function locally you will need to build the image
```
sam build --template template.yaml --use-container
```
Then to pass the environment variables to the container and invoke the function
User the following
```
sam local invoke --env-vars core/update_hiring/env.json
```