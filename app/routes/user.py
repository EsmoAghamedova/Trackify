from flask import Blueprint, render_template, redirect, url_for, flash

user_bp = Blueprint('user', __name__, url_prefix='/user')

@user_bp.route('/')
def user_dashboard():   
    return render_template('user/dashboard.html')

@user_bp.route('/profile')
def user_profile():
    return render_template('user/profile.html')

@user_bp.route('/shipment-create', methods=['GET', 'POST'])
def create_shipment():
    return render_template('user/shipment_create.html')

@user_bp.route('/shipments')
def user_shipments():
    return render_template('user/shipments_list.html')

@user_bp.route('/shipment/<int:shipment_id>')
def user_shipment_details(shipment_id):
    return render_template('user/shipment_detail.html', shipment_id=shipment_id)

@user_bp.route('/chats')
def user_chats():
    return render_template('user/chats.html') 

@user_bp.route('/chat/<int:chat_id>')
def user_chat_detail(chat_id):
    return render_template('user/chat.html', chat_id=chat_id)