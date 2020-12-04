
def dynamodb_stream_record_to_firehose(record):
    firehose_rec = {}

    for key, value in record.items():
        if "S" in value:
            firehose_rec[key] = value["S"]
        elif "N" in value:
            firehose_rec[key] = float(value["N"])
        elif "BOOL" in value:
            firehose_rec[key] = str(bool(value["BOOL"])).lower()
        elif "M" in value:
            firehose_rec[key] = dynamodb_stream_record_to_firehose(value["M"])
        else:
            ValueError("Unsupported attribute type")

    return firehose_rec
