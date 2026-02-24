from app import app,db
from flask import request, jsonify
from werkzeug.security import generate_password_hash,check_password_hash
from app.models.user import User
from flask_jwt_extended import create_access_token

# @app.route('/register',methods=['POST'])
@app.post('/register')
def register():
    data = request.get_json()
    check_email = User.query.filter_by(email=data['email']).first()
    if check_email:
        return jsonify(message="This email already exists")
    hashed_password = generate_password_hash(data['password'])
    new_user = User(first_name = data['first_name'],
                     last_name = data['last_name'],
                     email = data['email'],
                     password = hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify(message = "Registered Seccessfully"),201

@app.post('/login')
def login():
    data = request.get_json()
    if not data:
        return jsonify(message="Invalid or missing JSON data"),400
    email = data.get("email")
    password = data.get("password")
    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password,password):
        return jsonify(message="Invalid credentials")
    access_token = create_access_token(identity=email)
    return jsonify(message="Sucessful login", access_token=access_token)
