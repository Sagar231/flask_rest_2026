from flask import jsonify,request
from app import app, db,basic_auth
from app.models.country import Country
from app.schemas.country_schema import country_schema,countries_schema
from flask_jwt_extended import jwt_required

@app.route("/")
def home():
    return "Hellow, world!"

@app.route("/example")
def example():
    return jsonify(text="Good example", message="Final example"), 200

# @app.route("/countries", methods=["GET"])
@app.get("/countries")
@basic_auth.login_required()
def countries():
    country_list = Country.query.all()
    result = countries_schema.dump(country_list)
    return jsonify(result)

@app.route('/country_details/<int:id>',methods=['GET'])
@jwt_required()
def country_details(id: int):
    country = Country.query.filter_by(country_id = id).first()
    if country:
        result = country_schema.dump(country)
        return jsonify(result)
    return jsonify(message = "That country does not exist!"),404

# @app.post('/add_country')
@app.route('/add_country', methods=['POST'])
def add_country():
    country_name = request.form['country_name']
    check_country = Country.query.filter_by(country_name= country_name).first()
    if check_country:
        return jsonify(message = 'The country already exists in DB')
    capital = request.form['capital']
    area = request.form['area']

    new_country = Country(
        country_name=country_name,
        capital=capital,
        area=area
    )

    db.session.add(new_country)
    db.session.commit()

    return jsonify(message= 'You added a new country'), 201

@app.route('/add_country1',methods=['POST'])
def add_country1():
    data = request.get_json()
    if not data:
        return jsonify("Invalid or missing JSON DATA")
    country_name = data.get('country_name')
    check_country = Country.query.filter_by(country_name= country_name).first()
    if check_country:
        return jsonify(message = 'The country already exists in DB')
    capital = data.get('capital')
    area = data.get('area')
    new_country = Country(
        country_name=country_name,
        capital=capital,
        area=area
    )

    db.session.add(new_country)
    db.session.commit()
    return jsonify(message='You added a new country'),201

@app.route('/countries/<int:country_id>',methods=['PATCH'])
def update_country(country_id: int):
    data = request.get_json()
    country = Country.query.filter_by(country_id=country_id).first()
    if not country:
        return jsonify(message="Country not found"),404
    if 'country_name' in data:
        country.country_name = data['country_name']
    if 'capital' in data:
        country.capital = data['capital']
    if 'area' in data:
        country.area = data['area']
    db.session.commit()
    return jsonify(message= "Country updated successfully", country_id= country_id),200

@app.route('/remove_country/<int:country_id>',methods=['DELETE'])
def remove_country(country_id):
    country = Country.query.filter_by(country_id=country_id).first()
    if not country:
        return jsonify(message="Country not found"),404 
        #return {"message":"Country not found"},404     
    db.session.delete(country)
    db.session.commit()
    return jsonify(message= f"You deleted a country with id {country_id}"),202
