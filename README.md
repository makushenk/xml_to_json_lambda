
# AWS Lambda: XML to JSON 

## Maintenance

### Build an image container
```
docker build -t xml_to_json:latest .   
```

### Run container locally
```
docker run -p 9000:8080 xml_to_json:latest
```

### Test lambda function locally using [RIE](https://docs.aws.amazon.com/lambda/latest/dg/images-test.html)
```
curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}'
```

## Deployment

Lambda supports two types of deployment packages (see [documentation](https://docs.aws.amazon.com/lambda/latest/dg/getting-started.html))

<i>I would recommend using the first option because it's pretty much straightforward.</i>

### Deploy .zip file archive

1. Create deployment archive (you may need to run `chmod a+x mkda.sh`)
```
./mkda.sh
```

2. Deploy .zip file to the function (you may need to create lambda function [here](https://us-east-1.console.aws.amazon.com/lambda/home?region=us-east-1#/functions))
```
aws lambda update-function-code --function-name xml_to_json --zip-file fileb://deployment-package.zip
```

### Deploy container image

TBD
