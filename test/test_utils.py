from moto.core import ACCOUNT_ID


def create_redshift_delivery_stream(client, stream_name):
    return client.create_delivery_stream(
        DeliveryStreamName=stream_name,
        RedshiftDestinationConfiguration={
            "RoleARN": "arn:aws:iam::{}:role/firehose_delivery_role".format(ACCOUNT_ID),
            "ClusterJDBCURL": "jdbc:redshift://host.amazonaws.com:5439/database",
            "CopyCommand": {
                "DataTableName": "outputTable",
                "CopyOptions": "CSV DELIMITER ',' NULL '\\0'",
            },
            "Username": "username",
            "Password": "password",
            "S3Configuration": {
                "RoleARN": "arn:aws:iam::{}:role/firehose_delivery_role".format(
                    ACCOUNT_ID
                ),
                "BucketARN": "arn:aws:s3:::kinesis-test",
                "Prefix": "myFolder/",
                "BufferingHints": {"SizeInMBs": 123, "IntervalInSeconds": 124},
                "CompressionFormat": "UNCOMPRESSED",
            },
        },
    )


def create_delivery_stream(client, stream_name):
    return client.create_delivery_stream(
        DeliveryStreamName=stream_name,
        S3DestinationConfiguration={
            "RoleARN": f"arn:aws:iam::{ACCOUNT_ID}:role/firehose_delivery_role",
            "BucketARN": "arn:aws:s3:::kinesis-test",
            "Prefix": "myFolder/",
            "BufferingHints": {"SizeInMBs": 123, "IntervalInSeconds": 124},
            "CompressionFormat": "UNCOMPRESSED",
        }
    )
