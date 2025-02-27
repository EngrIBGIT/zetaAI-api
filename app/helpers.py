from .extensions.database import database, session
from flask import abort, jsonify



def is_valid_number(value):
    # Check if the value is a number
    return isinstance(value, (int, float))


def add_record_to_database(record):
    try:
        session.add(record)
        session.commit()
    except Exception as e:
        print(e)
        database.session.rollback()

def add_records_to_database(records):
    try:
        session.add_all(records)
        session.commit()
    except Exception as e:
        session.rollback()

    
def create_response(status: bool, message: str, data=None):
    response = {
        "status": status,
        "message": message
    }
    if data is not None:
        response["data"] = data
    return jsonify(response)
