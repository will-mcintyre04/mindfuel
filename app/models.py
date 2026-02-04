from .extensions import db

class Email(db.Model):
    '''Represents unique email address'''
    __tablename__ = "emails"
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(120), unique=True, nullable=False)