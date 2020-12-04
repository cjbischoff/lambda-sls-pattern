# AWS Lambda function to put data into Firehose

## Requirements

### `serverless` framework

- To install _serverless_ globally with `npm`

  - `npm install serverless -g`

## Tests

- To run unit tests
  - `docker build -f test/Dockerfile -t qt-tests-lambda .`
  - `docker run -t qt-tests-lambda`

## Local Run

### Invoke function locally

- `serverless invoke local --function TestsHandler --path test/test_data/dynamo_stream_data.json`
