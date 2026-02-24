from app import app,db
from app.models.user import User
from app.models.country import Country

@app.cli.command("db_create")
def db_create():
    db.create_all()
    print("database created")

@app.cli.command("db_drop")
def db_drop():
    db.drop_all()
    print("database dropped!")

@app.cli.command("db_seed")
def db_seed():
    usa = Country(country_name="USA", capital="Washington", area=378967)
    france = Country(country_name="France", capital="Paris", area=36748)

    db.session.add(usa)
    db.session.add(france)

    first_user = User(
        first_name="Divu",
        last_name="Baby",
        email="divubaby@gmil.com",
        password="SagarBaby",
    )
    db.session.add(first_user)
    db.session.commit()
    print("Database Seeded!")

@app.cli.command("db_read")
def db_read():
    print("Countries:")
    countries = Country.query.all()
    for c in countries:
        print(c.country_id, c.country_name, c.capital, c.area)

    print("\nUsers:")
    users = User.query.all()
    for u in users:
        print(u.id, u.first_name, u.last_name, u.email)