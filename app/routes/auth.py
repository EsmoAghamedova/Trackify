from flask import render_template, Blueprint, redirect, url_for, flash, session

auth_bp = Blueprint('auth', __name__)
@auth_bp.route('/register')
def register():
    return render_template('/auth/register.html')

@auth_bp.route('/login')
def login():
    return render_template('/auth/login.html')

@auth_bp.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('public.home'))