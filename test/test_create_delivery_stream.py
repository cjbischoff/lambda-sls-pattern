from unittest import TestCase

import boto3
from moto import mock_kinesis
from moto.core import ACCOUNT_ID
import sure

from test.test_utils import create_delivery_stream


class CreateDeliveryStreamTestCase(TestCase):

    @mock_kinesis
    def test_create_delivery_stream(self):
        client = boto3.client("firehose", region_name="us-west-2")

        response = create_delivery_stream(client, "stream1")
        stream_arn = response["DeliveryStreamARN"]

        response = client.describe_delivery_stream(DeliveryStreamName="stream1")
        stream_description = response["DeliveryStreamDescription"]

        # Sure and Freezegun don't play nicely together
        _ = stream_description.pop("CreateTimestamp")
        _ = stream_description.pop("LastUpdateTimestamp")

        stream_description.should.equal(
            {
                "DeliveryStreamName": "stream1",
                "DeliveryStreamARN": stream_arn,
                "DeliveryStreamStatus": "ACTIVE",
                "VersionId": "string",
                "Destinations": [
                    {
                        "DestinationId": "string",
                        "S3DestinationDescription": {
                            "RoleARN": "arn:aws:iam::{}:role/firehose_delivery_role".format(
                                ACCOUNT_ID
                            ),
                            "RoleARN": "arn:aws:iam::{}:role/firehose_delivery_role".format(
                                ACCOUNT_ID
                            ),
                            "BucketARN": "arn:aws:s3:::kinesis-test",
                            "Prefix": "myFolder/",
                            "BufferingHints": {"SizeInMBs": 123, "IntervalInSeconds": 124},
                            "CompressionFormat": "UNCOMPRESSED",
                        },
                    }
                ],
                "HasMoreDestinations": False,
            }
        )
