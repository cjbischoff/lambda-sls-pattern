from unittest import TestCase

import sure

from test.test_lambda_handler import dynamodb_stream_data
from src.converter.converter import dynamodb_stream_record_to_firehose

expected_firehose_record = {
    "autoAllocationEnabled": "false",
    "autoAllocationGlobal": "false",
    "autoAllocationTrafficPercent": 100,
    "cells": {
        "Control": 50,
        "Treatment": 50
    },
    "changes": {
        "2020-06-16T13:25:25.254Z": {
            "author": "admin",
            "fieldChanges": "{\"1\":{\"lst\":[\"rec\",13,{\"1\":{\"str\":\"name\"},\"3\":{\"str\":\"AUTH3404_2SV_with_TOTP_TEST1\"}},{\"1\":{\"str\":\"status\"},\"3\":{\"str\":\"Dormant\"}},{\"1\":{\"str\":\"autoAllocationEnabled\"},\"3\":{\"str\":\"false\"}},{\"1\":{\"str\":\"autoAllocationGlobal\"},\"3\":{\"str\":\"false\"}},{\"1\":{\"str\":\"autoAllocationTrafficPercent\"},\"3\":{\"str\":\"100\"}},{\"1\":{\"str\":\"autoAllocationTotalThreshold\"},\"3\":{\"str\":\"0\"}},{\"1\":{\"str\":\"forUsers\"},\"3\":{\"str\":\"true\"}},{\"1\":{\"str\":\"forVisitors\"},\"3\":{\"str\":\"false\"}},{\"1\":{\"str\":\"cells\"},\"3\":{\"str\":\"[TCell(name:Control, allocationPercent:50), TCell(name:Treatment, allocationPercent:50)]\"}},{\"1\":{\"str\":\"defaultCellName\"},\"3\":{\"str\":\"Control\"}},{\"1\":{\"str\":\"isDefaultForced\"},\"3\":{\"str\":\"false\"}},{\"1\":{\"str\":\"forOrganizations\"},\"3\":{\"str\":\"false\"}},{\"1\":{\"str\":\"jiraId\"},\"3\":{\"str\":\"N/A\"}}]}}"
        },
        "2020-06-16T13:26:29.343Z": {
            "author": "admin",
            "fieldChanges": "{\"1\":{\"lst\":[\"rec\",1,{\"1\":{\"str\":\"status\"},\"2\":{\"str\":\"Dormant\"},\"3\":{\"str\":\"Live\"}}]}}"
        }
    },
    "creationTime": "2020-06-16T13:25:25.254Z",
    "defaultCellName": "Control",
    "defaultForced": "false",
    "description": "N/A",
    "forOrganizations": "false",
    "forUsers": "true",
    "forVisitors": "false",
    "jiraId": "N/A",
    "lastUpdateTime": "2020-06-16T13:26:29.343Z",
    "lowerCaseDescription": "n/a",
    "lowerCaseTestName": "auth3404_2sv_with_totp_test1",
    "testName": "AUTH3404_2SV_with_TOTP_TEST1",
    "testOwner": "N/A",
    "testStatus": 2
}


class DynamodbFirehoseConverterTestCase(TestCase):

    def test_dynamo_to_firehose(self):
        record = dynamodb_stream_data['Records'][0]["dynamodb"]["NewImage"]

        converted_record = dynamodb_stream_record_to_firehose(record)

        converted_record.should.equal(expected_firehose_record)
