import json

event = {
    "Records": [
        {
            "eventVersion": "2.1",
            "eventSource": "aws:s3",
            "awsRegion": "us-east-2",
            "eventTime": "2019-09-03T19:37:27.192Z",
            "eventName": "ObjectCreated:Put",
            "userIdentity": {
                "principalId": "AWS:AIDAINPONIXQXHT3IKHL2"
            },
            "requestParameters": {
                "sourceIPAddress": "205.255.255.255"
            },
            "responseElements": {
                "x-amz-request-id": "D82B88E5F771F645",
                "x-amz-id-2": "vlR7PnpV2Ce81l0PRw6jlUpck7Jo5ZsQjryTjKlc5aLWGVHPZLj5NeC6qMa0emYBDXOo6QBU0Wo="
            },
            "s3": {
                "s3SchemaVersion": "1.0",
                "configurationId": "828aa6fc-f7b5-4305-8584-487c791949c1",
                "bucket": {
                    "name": "lambda-artifacts-deafc19498e3f2df",
                    "ownerIdentity": {
                        "principalId": "A3I5XTEXAMAI3E"
                    },
                    "arn": "arn:aws:s3:::lambda-artifacts-deafc19498e3f2df"
                },
                "object": {
                    "key": "b21b84d653bb07b05b1e6b33684dc11b",
                    "size": 1305107,
                    "eTag": "b21b84d653bb07b05b1e6b33684dc11b",
                    "sequencer": "0C0F6F405D6ED209E1"
                }
            }
        }
    ]
}



print(event["Records"][0]["s3"]["bucket"])

week_dictionary = {
    "day": [
        {
            "message": "Beautiful Monday"
        },
        {
            "message": "Learning Tuesday"
        },
        {
            "message": "Studious Wednesday"
        },
        {
            "message": "Tiresome Thursday"
        },
        {
            "message": "Futuristic Friday"
        },
        {
            "message": "soothing saturday"
        }
    ],
    "mon": "Monday",
    "tue": "Tuesday",
    "wed": "Wednesday",
    "thur": "Thursday",
    "fri": "friday",
    "sat": "Saturday",
    "sun": "Sunday",
    0:"powerful number"
}

print(week_dictionary.get("Mon","Not a valid Key"))
print(week_dictionary.get("day")[2].get("message"))
print(week_dictionary.get(0))


json_week=json.dumps(week_dictionary)
print(json_week)