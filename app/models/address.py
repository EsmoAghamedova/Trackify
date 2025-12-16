from app.extensions import db

class Address(db.Model):
    __tablename__ = 'addresses'

    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(80), nullable=False)
    country = db.Column(db.String(2), nullable=False)  # ISO2
    street = db.Column(db.String(150))
    postal_code = db.Column(db.String(20))

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
