from . import routes_blueprint
from ..services import chat
from flask import request
# from flask_parameter_validation import ValidateParameters, Query
from typing import Optional
from ..error_handler import url_validation_error_handler
from ..helpers import create_response
from ..constants import SUCCESS_MESSAGE
from ..enums import CustomStatusCode

@routes_blueprint.route('/chat-history', methods=['GET'])
def fetch_chat_history():
    response = chat.fetch_chat_history(request.args.get('username'))
    return create_response(CustomStatusCode.SUCCESS.value, SUCCESS_MESSAGE, response), 200

@routes_blueprint.route('/chat', methods=['POST'])
def prompt_bot():
    response = chat.prompt_bot(request.get_json())
    return create_response(CustomStatusCode.SUCCESS.value, SUCCESS_MESSAGE, response), 200

