from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://heyumm:heyumm@localhost:5432/heyumm'
db = SQLAlchemy(app)

class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    msg = db.Column(db.String(80))

    def __init__(self, id, msg):
        self.id= id
        self.msg = msg

    def __repr__(self):
        return '<Test id: {0}, msg: {1}>'.format(self.id, self.msg)

@app.route("/")
def hello():
    return "Hello"

if __name__ == "__main__": #when runpy
    db.create_all()
    one = Test(1, 'Hello, World!')
    two = Test(2, 'kkyu')
    db.session.add(one)
    db.session.add(two)
    db.session.commit()
    app.run(host = '0.0.0.0')


