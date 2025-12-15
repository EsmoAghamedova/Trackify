from flask import Blueprint, render_template, redirect, url_for, flash

company_bp = Blueprint('company', __name__, url_prefix='/company')

@company_bp.route('/')
def company_dashboard():
    return render_template('company/dashboard.html')

@company_bp.route('/profile')
def company_profile():
    return render_template('company/profile.html')

@company_bp.route('/shipments')
def manage_shipments():
    return render_template('company/shipments_list.html')

@company_bp.route('/shipment/<int:shipment_id>')
def shipment_details(shipment_id):
    return render_template('company/shipment_detail.html', shipment_id=shipment_id)

@company_bp.route('/chats')
def company_chats():
    return render_template('company/chats.html')

@company_bp.route('/chat/<int:chat_id>')
def company_chat_detail(chat_id):
    return render_template('company/chat.html', chat_id=chat_id)