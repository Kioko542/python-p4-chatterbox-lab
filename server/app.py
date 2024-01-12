from flask import Flask, request, make_response, jsonify
from flask_cors import CORS
from flask_migrate import Migrate

from models import db, Message

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)
migrate = Migrate(app, db)

db.init_app(app)

# GET all messages
@app.route('/messages')
def get_messages():
    messages = Message.query.all()
    messages_serialized = [message.to_dict() for message in messages]
    return make_response(jsonify(messages_serialized), 200)

# GET message by ID
@app.route('/messages/<int:id>')
def get_message_by_id(id):
    message = Message.query.get(id)
    if message:
        return make_response(jsonify(message.to_dict()), 200)
    else:
        return make_response(jsonify({'error': 'Message not found'}), 404)

# POST create a new message
@app.route('/messages', methods=['POST'])
def create_message():
    data = request.json
    new_message = Message(body=data.get('body'), username=data.get('username'))
    db.session.add(new_message)
    db.session.commit()
    return make_response(jsonify(new_message.to_dict()), 201)

# PATCH update the body of a message
@app.route('/messages/<int:id>', methods=['PATCH'])
def update_message(id):
    message = Message.query.get(id)
    if message:
        data = request.json
        message.body = data.get('body', message.body)
        db.session.commit()
        return make_response(jsonify(message.to_dict()), 200)
    else:
        return make_response(jsonify({'error': 'Message not found'}), 404)

# DELETE a message
@app.route('/messages/<int:id>', methods=['DELETE'])
def delete_message(id):
    message = Message.query.get(id)
    if message:
        db.session.delete(message)
        db.session.commit()
        return make_response(jsonify({'message': 'Message deleted successfully'}), 200)
    else:
        return make_response(jsonify({'error': 'Message not found'}), 404)

if __name__ == '__main__':
    app.run(port=5555)
