import os 

#Database
DATABASE_URL = os.getenv('DATABASE_URL')

#Flask Config
APP_SECRET_KEY = os.getenv('SECRET_KEY')

#Repsonse Messages
NOT_FOUND_MESSAGE = 'Not found'
SUCCESS_MESSAGE = 'Success'
INTERNAL_SERVER_ERROR_MESSAGE = 'Something went wrong'

