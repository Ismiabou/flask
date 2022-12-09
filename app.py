from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123688mr@localhost/commentary'
db = SQLAlchemy(app)


class Data(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    name = db.Column(db.String(30))
    comment = db.Column(db.String(400))

    def __init__(self, email, name, comment):
        self.email = email
        self.name = name
        self.comment = comment


def add():
    if request.method == 'POST':
        email = request.form["email"]
        name = request.form["name"]
        comment = request.form["comment"]
        if db.session.query(Data).filter(Data.email == email).count() == 0:
            data = Data(email, name, comment)
            db.session.add(data)
            db.session.commit()


@app.route('/', methods=['GET', 'POST'])
def iee():
    add()
    posts = Data.query.all()

    return render_template("Home.html", posts=posts)


@app.route('/home', methods=['GET', 'POST'])
def home():
    add()
    posts = Data.query.all()
    return render_template("Home.html", posts=posts)


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
