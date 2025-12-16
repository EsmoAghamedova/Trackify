from app.extensions import db
from datetime import datetime

class Message(db.Model):
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True)

    # sender info
    sender_type = db.Column(db.String(20), nullable=False)  # USER | COMPANY | ADMIN
    sender_id = db.Column(db.Integer, nullable=False)

    # receiver info
    receiver_type = db.Column(db.String(20), nullable=False)
    receiver_id = db.Column(db.Integer, nullable=False)

    # context
    shipment_id = db.Column(db.Integer, db.ForeignKey('parcel_requests.id'))
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'))

    text = db.Column(db.Text, nullable=False)
    is_read = db.Column(db.Boolean, default=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
