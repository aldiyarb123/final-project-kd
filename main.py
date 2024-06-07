from flask import Flask, render_template,  request, redirect
#Подключение библиотеки базы данных
from flask_sqlalchemy import SQLAlchemy
from uran import *

app = Flask(__name__)
#Подключение SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#Создание db
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST', "GET"])
def process_form():
    gram = request.form.get('gram')
    return render_template('index.html', gram=photon_energy(int(gram)))

if __name__ == "__main__":
    app.run(debug=True)