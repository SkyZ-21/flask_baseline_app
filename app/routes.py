from flask import Blueprint

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return 'Welcome, thank you for visiting!'

@main.route('/health')
def health():
    return {'status': 'healthy'}

@main.route('/status')
def status():
    return {'status': 'healthy', 'app': 'flask_baseline_app'}

@main.route('/about')
def about():
    return {'message': 'My first project, constructive feedback encouraged'}
