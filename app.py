from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from email_sending import send_email


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:e9HZCpumYLyes19UaVjJ@containers-us-west-125.railway' \
                                        '.app:7876/railway '
db = SQLAlchemy(app)


class Data(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    name = db.Column(db.String(30))
    comment = db.Column(db.String(400))

    def __init__(self, name, email, comment):
        self.name = name
        self.email = email
        self.comment = comment


@app.route('/', methods=['GET'])
def iee():
    return render_template("Home.html")


@app.route('/home', methods=['POST'])
def home():
    if request.method == 'POST':
        comment = request.form["comment"]
        name = request.form["name"]
        email = request.form["email"]
        if db.session.query(Data).filter(Data.email == email).count() == 0:
            data = Data(comment, name, email)
            db.session.add(data)
            db.session.commit()
            send_email(email, thanking_)
            return render_template("Home.html")
    return render_template("Home.html")


@app.route('/installation', methods=['GET'])
def installation():
    return render_template("Installation.html")


@app.route('/market', methods=['GET'])
def market():
    return render_template("Market.html")


@app.route('/maintenance', methods=['GET'])
def maintenance():
    return render_template("Maintenance.html")


@app.route('/about', methods=['GET'])
def about():
    return render_template("About.html")


@app.route('/support', methods=['GET'])
def support():
    return render_template("Support.html")


if __name__ == "__main__":
    app.run(debug=True)
