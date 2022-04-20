from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "this is not a secret"


ENV = 'prod'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/report'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://beetqyoqzvaojb:331360c2c8b4955109c94cc1354aa1ff3bbaefad2ee556b3b5f9d2c71c6144db@ec2-34-194-158-176.compute-1.amazonaws.com:5432/d9chjgndae7a8p'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Reports(db.Model):
    __tablename__ = 'report'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    location = db.Column(db.String)
    chlorine = db.Column(db.String)
    meterValues = db.Column(db.Float)
    chlorineValues = db.Column(db.Float)

    def __init__(self, date, location, chlorine, meterValues, chlorineValues):
        self.date = date
        self.location = location
        self.chlorine = chlorine
        self.meterValues = meterValues
        self.chlorineValues = chlorineValues


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        date = request.form['date']
        location = request.form['location']
        chlorine = request.form['chlorine']
        meterValues = request.form['meterValues']
        chlorineValues = request.form['chlorineValues']
        #print(date, location, chlorine, meterValues, chlorineValues)
        if date == '':
            return render_template('index.html', message='Please enter date.')
        return render_template('success.html')

if __name__ == '__main__':
    app.run()
