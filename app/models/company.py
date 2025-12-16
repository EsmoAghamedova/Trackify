from app.extensions import db

class Company(db.Model):
    __tablename__ = "companies"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20))
    role = db.Column(db.String(30), default='COMPANY_ADMIN')

    logo_url = db.Column(db.String(255))

    base_price = db.Column(db.Float, default=0)
    price_per_kg = db.Column(db.Float, default=0)
    fuel_pct = db.Column(db.Float, default=0)
    insurance_pct = db.Column(db.Float, default=0)

    hq_address_id = db.Column(db.Integer, db.ForeignKey('addresses.id'))

    parcel_requests = db.relationship('ParcelRequest', backref='company', lazy=True)