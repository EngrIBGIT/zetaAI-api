from ..extensions.database import database
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import jsonpickle

class User(database.Model):
    __tablename__ = 'users'

    id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    username = database.Column(database.String(255), nullable=False, unique=True)
    chat_memory = database.Column(database.Text, nullable=True)

    def __repr__(self):
        return f'<User {self.id}>'
    
    def serialize(self):
        return {
            'username': self.username,
            'chat_memory': self.deserialize_chat_memory()
        }
    
    def save_chat_memory(self, chat_data):
        self.chat_memory = jsonpickle.encode(chat_data)

    def deserialize_chat_memory(self):
        """Retrieve chat memory, handling empty cases"""
        if not self.chat_memory:
            return None  # Return an empty list if there's no stored chat memory
        try:
            return jsonpickle.decode(self.chat_memory)
        except Exception as e:
            print(f"Error decoding chat memory: {e}")
            return None