import json
from unittest import TestCase
from unittest.mock import patch, ANY

from src.lambda_handler import handle

with open("test/test_data/dynamo_stream_data.json", "rb") as json_file:
    dynamodb_stream_data = json.load(json_file)


class LambdaHandlerTestCase(TestCase):
    DEFAULT_CONTEXT = {}

    @patch("src.lambda_handler.put_firehose_record")
    def test_lambda_handler(self, put_firehose_record):
        handle(dynamodb_stream_data, self.DEFAULT_CONTEXT)
        put_firehose_record.assert_called_once_with(ANY)
