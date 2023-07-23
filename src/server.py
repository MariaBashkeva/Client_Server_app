from flask import Flask, request, jsonify
import socket
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user

app = Flask(__name__)

connected_clients = {}

@app.route('/api', methods=['GET'])
def receive_client_data():
    data = request.get_data()

    return jsonify({'status': 'success'})

@app.route('/')
def receive_data():
    raw_data = request.get_data() 
    processed_data = raw_data.decode('utf-8')

    return f'Received data: {processed_data}'

@app.route('/api/request_screenshot/<client_id>', methods=['GET'])
def request_screenshot(client_id):
    return jsonify({'status': 'success'})

@app.route('/clients', methods=['GET'])
def list_connected_clients():

    return jsonify(connected_clients)


@app.route('/domain', methods=['GET'])
def domain():
    user_domain = request.headers.get('Host', '')
    return jsonify({'domain': user_domain})

@app.route('/machine', methods=['GET'])
def machine():
    user_machine = socket.gethostname()
    return jsonify({'machine': user_machine})

@app.route('/ip', methods=['GET'])
def ip():
    user_ip = request.remote_addr
    return jsonify({'ip': user_ip})

app.secret_key = 'your_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin):
    def __init__(self, id):
        self.id = id

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route('/login', methods=['POST'])
def login():
    user_id = request.form.get('user_id')
    user = User(user_id)
    login_user(user)
    return jsonify({'message': 'Login successful'})


@app.route('/get_current_user', methods=['GET'])
@login_required
def get_current_user():
    return jsonify({'user_id': current_user.id})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)