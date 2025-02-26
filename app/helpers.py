from .extensions.database import database
from flask import abort, jsonify



def is_valid_number(value):
    # Check if the value is a number
    return isinstance(value, (int, float))


def add_record_to_database(record):
    try:
        database.session.add(record)
        database.session.commit()
    except Exception as e:
        print(e)
        database.session.rollback()

def add_records_to_database(records):
    try:
        database.session.add_all(records)
        database.session.commit()
    except Exception as e:
        database.session.rollback()

    
def create_response(status: bool, message: str, data=None):
    response = {
        "status": status,
        "message": message
    }
    if data is not None:
        response["data"] = data
    return jsonify(response)
