from sqlalchemy.dialects.postgresql import JSON
from ..extensions.database import database
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

class Conversation(database.Model):
    __tablename__ = 'conversations'

    id = database.Column(database.Integer, primary_key=True)
    user_id = database.Column(database.Integer, database.ForeignKey('users.id'), nullable=False) 
    title = database.Column(database.String(255), nullable=True, default="New Chat")
    memory = database.Column(database.JSON, nullable=False)
    created_at = database.Column(database.DateTime(timezone=True), server_default=func.now())
    updated_at = database.Column(database.DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    user = relationship("User", back_populates='conversations')

    def __repr__(self):
        return f'<Conservation {self.id}>'