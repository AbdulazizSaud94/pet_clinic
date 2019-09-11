from flask import Flask, render_template, request, session, redirect
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/animalclinic'
db = SQLAlchemy(app)

class Pets(db.Model):
    pet_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    type = db.Column(db.String(45))
    created_at = db.Column(default=datetime.datetime.now())
    updated_at = db.Column(default=datetime.datetime.now())
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def __repr__(self):
        return '<Pet %r>' % self.email

@app.route('/')                           
def index():
    # pet = Pets('Boboy', 'Dog')
    # db.session.add(pet)
    # db.session.commit()
    all_pets = Pets.query.all()
    return render_template('index.html', pets = all_pets)

@app.route('/add_pet', methods=["POST"])
def add_pet():
    pet = Pets(request.form['name'], request.form['type'])
    db.session.add(pet)
    db.session.commit()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)