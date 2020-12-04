from unittest import TestCase
from moto import mock_kinesis
from unittest.mock import patch
import os

import boto3

from test.test_utils import create_delivery_stream
from src.firehose.firehose_producer import put_firehose_record

STREAM_NAME = "stream1"
REGION_NAME = "us-west-2"


class PutFirehoseTestCase(TestCase):

    @patch('src.firehose.firehose_producer.delivery_stream_name', STREAM_NAME)
    @patch('src.firehose.firehose_producer.region_name', REGION_NAME)
    @mock_kinesis
    def test_put_firehose(self):
        client = boto3.client("firehose", region_name=REGION_NAME)
        create_delivery_stream(client, STREAM_NAME)

        firehose_record = {
            "X": "A",
            "Y": "B",
            "Z": "C"
        }
        put_firehose_record(firehose_record)

