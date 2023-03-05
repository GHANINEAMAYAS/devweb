from flask import Flask, render_template,redirect, url_for,request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select
from sqlalchemy import desc
import os
import random,json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db=SQLAlchemy(app)
#db.init_app(app)

class Data(db.Model):
    __tablename__ = "data"

    id = db.Column(db.Integer, primary_key=True)
    rna_id = db.Column(db.String(30), nullable=True) 
    rna_id_ex = db.Column(db.String(30), nullable=True)
    gestion = db.Column(db.String(20), nullable=True)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/assos')
def assos():
    #stmt = select(Data)
    #datas = Data.query.limit(10).all()
    datas = Data.query.limit(10).all()
  
    return render_template('assos.html', datas=datas)
    #result = db.session.execute(stmt)
    #for data in datas:
     #   print(f"{data.rna_id}")
    #return render_template('assos.html')
@app.route('/delete_data/<int:id>', methods=['POST'])
@app.route('/delete/<int:data_id>')
def delete(data_id):
    data = Data.query.get(data_id)
    db.session.delete(data)
    db.session.commit()
    return redirect(url_for('assos'))
@app.route('/add_data', methods=['GET', 'POST'])
def add_data():
    if request.method == 'POST':
        rna_id = request.form['rna_id']
        rna_id_ex = request.form['rna_id_ex']
        gestion = request.form['gestion']

        # Créer un objet Data et l'ajouter à la base de données
        data = Data(rna_id=rna_id, rna_id_ex=rna_id_ex, gestion=gestion)
        db.session.add(data)
        db.session.commit()

        # Rediriger vers la page principale
        return redirect(url_for('assos'))

    return render_template('add_data.html')
@app.route('/modifier/<int:data_id>', methods=['GET', 'POST'])
def modifier(data_id):
    data = Data.query.get(data_id)

    if request.method == 'POST':
        data.rna_id = request.form['rna_id']
        data.rna_id_ex = request.form['rna_id_ex']
        data.gestion = request.form['gestion']
        db.session.commit()
        return redirect(url_for('assos'))
    return render_template('modifier.html', data=data)

@app.route('/piechart')
def piechart():
    datas = Data.query.order_by(desc(Data.id)).limit(10).all()
    labels = []
    values = []
    for data in datas:
        labels.append(data.gestion)
        values.append(data.id)

    return render_template('piechart.html', labels=labels, values=values)


@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
if __name__ == '__main__':
    app.run()  


