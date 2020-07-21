from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///C:/Users/Jonathan/coding/tests/site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class User(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    name=db.Column(db.String(25),nullable=False)
    age=db.Column(db.Integer())

def create_user(name,age):
    new_user=User(name=name,age=age)
    return new_user

@app.route('/<string:name>')
def hello(name):
    return "Hello {}".format(name)

@app.route('/signup/<string:name>/<int:age>')
def create_account(name,age):
    new_user=create_user(name,age)
    db.session.add(new_user)
    db.session.commit()
    return "Created user {}".format(new_user.name)

if __name__ == "__main__":
    app.run()