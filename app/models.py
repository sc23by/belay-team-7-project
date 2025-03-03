from app import db
from flask_login import UserMixin
from sqlalchemy import ForeignKey

# User model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    priority = db.Column(db.Integer, nullable=False, default=1)
    profile_picture = db.Column(db.String(255), nullable=False, default="default_profile.jpg")

# Expert model
class Expert(db.Model):
    expert_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'), unique=True, nullable=False)  # Each expert must be a unique user
    availability = db.Column(db.String(50), nullable=False)

# Payment Info model
class PaymentInfo(db.Model):
    payment_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'), unique=True, nullable=False)  # One user should have one payment info
    payment_type = db.Column(db.String(30), nullable=False)
    shipping_address = db.Column(db.String(500), nullable=False)

# Sold item model
class Solditem(db.Model):
    sold_id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, ForeignKey('item.item_id'), nullable=False)
    seller_id = db.Column(db.Integer, ForeignKey('user.id'), nullable=False)
    buyer_id = db.Column(db.Integer, ForeignKey('user.id'), nullable=False)
    price = db.Column(db.Float, nullable=False)

# item model
class Item(db.Model):
    item_id = db.Column(db.Integer, primary_key=True)
    seller_id = db.Column(db.Integer, ForeignKey('user.id'), nullable=False)
    item_name = db.Column(db.String(100), nullable=False)  # Removed unique constraint so same name can be reused
    minimum_price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    item_image = db.Column(db.String(500), nullable=False)
    duration = db.Column(db.Time, nullable=False)
    time = db.Column(db.Time, nullable=False)
    date = db.Column(db.Date, nullable=False)
    approved = db.Column(db.Boolean, default=False)
    shipping_cost = db.Column(db.Float, nullable=False)
    expert_payment_percentage = db.Column(db.Float, nullable=False, default=0.1) # Default can be changed by managers
    
    def get_image_url(self):
        return url_for('static', filename=f'images/items/{self.item_image}')

# Bids model
class Bids(db.Model):
    bid_id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, ForeignKey('item.item_id'), nullable=False)
    user_id = db.Column(db.Integer, ForeignKey('user.id'), nullable=False)
    bid_amount = db.Column(db.Float, nullable=False)  # Allows precise bid values
    bid_time = db.Column(db.Time, nullable=False)
    bid_date = db.Column(db.Date, nullable=False)
