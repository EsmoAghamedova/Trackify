from app.extensions import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    full_name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    role = db.Column(db.String(50), default='user') 
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    adresses = db.relationship('Address', backref='user', lazy=True)
    parcel_requests = db.relationship('ParcelRequest', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'