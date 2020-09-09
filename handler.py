import os
import json
from uszipcode import SearchEngine


def get(event, context):
    try:
        req_zipcode = event['pathParameters']['id']

        zipcode_db_dir = os.path.join(os.path.dirname(__file__), ".uszipcode")

        search = SearchEngine(simple_zipcode=True, db_file_dir=zipcode_db_dir)

        zipcode = search.by_zipcode(req_zipcode)

        search.close()

        if zipcode.to_dict()['zipcode'] is not None:
            rlt = zipcode.to_dict()

            print(rlt)
        else:
            rlt = ''

        statusCode = 200

    except Exception as e:
        print('[Error] ' + str(e))
        statusCode = 400
        rlt = ''

    response = {
        "statusCode": statusCode,
        "body": json.dumps(rlt)
    }

    return response
