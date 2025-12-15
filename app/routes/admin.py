from flask import Blueprint, render_template, redirect, url_for, flash

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/')
def admin_dashboard():
    return render_template('admin/dashboard.html')

@admin_bp.route('/users')
def manage_users(): 
    return render_template('admin/users.html')

@admin_bp.route('/companies')
def manage_companies():
    return render_template('admin/companies.html')

@admin_bp.route('/edit-user/<int:user_id>', methods=['GET', 'POST'])
def edit_user(user_id):
    return render_template('admin/edit_user.html', user_id=user_id)

@admin_bp.route('/edit-company/<int:company_id>', methods=['GET', 'POST'])
def edit_company(company_id):
    return render_template('admin/edit_company.html', company_id=company_id)

@admin_bp.route('/chats')
def manage_chats():
    return render_template('admin/chats.html')

@admin_bp.route('/chat/<int:chat_id>')
def admin_chat_detail(chat_id):
    return render_template('admin/chat.html', chat_id=chat_id)

@admin_bp.route('pricing')
def manage_pricing():
    return render_template('admin/pricing.html')