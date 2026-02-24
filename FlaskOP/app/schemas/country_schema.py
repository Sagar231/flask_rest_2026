from app import ma
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.country import Country

class CountrySchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Country 
        load_instance = True

country_schema = CountrySchema()
countries_schema = CountrySchema(many=True)
