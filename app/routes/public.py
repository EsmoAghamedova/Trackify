from flask import Blueprint, render_template, redirect, url_for, flash

public_bp = Blueprint('public', __name__)

@public_bp.route('/')
def home():
    return render_template('public/home.html')

@public_bp.route('/about')
def about():
    return render_template('public/about.html')

@public_bp.route('/pricing')
def pricing():
    return render_template('public/pricing.html')

@public_bp.route('/track')
def track():
    return render_template('public/track.html')

@public_bp.route('/faq')
def faq():
    return render_template('public/faq.html')

@public_bp.route('/contact')
def contact():
    return render_template('public/contact.html')