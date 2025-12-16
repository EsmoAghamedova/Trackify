from app.extensions import db
from datetime import datetime
from .enums import ShippingType, ParcelKind, RequestStatus

class ParcelRequest(db.Model):
    __tablename__ = 'parcel_requests'

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'))

    shipping_type = db.Column(db.Enum(ShippingType), nullable=False)
    status = db.Column(db.Enum(RequestStatus), default=RequestStatus.PENDING_REVIEW)

    weight_kg = db.Column(db.Float, nullable=False)
    length_cm = db.Column(db.Float, nullable=False)
    width_cm = db.Column(db.Float, nullable=False)
    height_cm = db.Column(db.Float, nullable=False)

    kind = db.Column(db.Enum(ParcelKind), nullable=False)
    declared_value = db.Column(db.Float)
    fragile = db.Column(db.Boolean, default=False)

    origin_address_id = db.Column(db.Integer, db.ForeignKey('addresses.id'))
    destination_address_id = db.Column(db.Integer, db.ForeignKey('addresses.id'))
    pickup_address_id = db.Column(db.Integer, db.ForeignKey('addresses.id'))
    delivery_address_id = db.Column(db.Integer, db.ForeignKey('addresses.id'))

    tracking_id = db.Column(db.String(100), unique=True)
    review_comment = db.Column(db.Text)
    
    messages = db.relationship('Message', backref='shipment', lazy=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
