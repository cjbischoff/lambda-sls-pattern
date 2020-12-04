from log_cfg import logger

from src.converter.converter import dynamodb_stream_record_to_firehose
from src.firehose.firehose_producer import put_firehose_record


def handle(event, context):
    records = event.get('Records', [])

    if not records:
        return {
            "status": 200,
            "message": "No records found!"
        }

    for record in records:
        event_name = record["eventName"]
        logger.info(f"Event name: {event_name}")

        record_to_convert = record["dynamodb"]["NewImage"]
        firehose_record = dynamodb_stream_record_to_firehose(record_to_convert)

        try:
            logger.info(firehose_record)
            put_firehose_record(firehose_record)
        except BaseException as error:
            logger.error(error)
            return {
                "status": "500",
                "message": "Something went wrong!"
            }

    return {
        "status": 200,
        "message": "All records are put to firehose"
    }
