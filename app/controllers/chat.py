from . import routes_blueprint
from ..services import chat
# from flask_parameter_validation import ValidateParameters, Query
from typing import Optional
from ..error_handler import url_validation_error_handler
from ..helpers import create_response
from ..constants import SUCCESS_MESSAGE
from ..enums import CustomStatusCode


@routes_blueprint.route('/chat', methods=['POST'])
def get_notifications():
    response = chat.start_chat(1, 'how are you>', 'pirate')
    return create_response(CustomStatusCode.SUCCESS.value, SUCCESS_MESSAGE, response), 200