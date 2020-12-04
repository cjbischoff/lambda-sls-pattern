import datetime
import json
import os

import boto3

from log_cfg import logger

delivery_stream_name = os.environ.get("FIREHOSE_DELIVERY_STREAM_NAME", "stream1")
region_name = os.environ.get("REGION", "us-west-2")


def put_firehose_record(firehose_record):
    timestamp = round(datetime.datetime.utcnow().timestamp() * 1000)
    client = boto3.client("firehose", region_name=region_name)

    try:
        client.put_record(
            DeliveryStreamName=delivery_stream_name,
            Record={
                "Data": json.dumps(firehose_record, ensure_ascii=False) + "\n"
            }
        )
        logger.info(timestamp)
    except BaseException as error:
        logger.error(f"An exception occured: {error}")
        raise error
