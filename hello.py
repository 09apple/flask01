from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/demo?charset=utf8'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)
class Role(db.Model):
    __tablename__ = 'roles'
    __charset__ ='utf8'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))

    def __repr__(self):
        return '<Role %r>' % self.name

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))

    def __repr__(self):
        return '<User %r>' % self.username

@app.route('/add')
def add():
    db.create_all()
    return '<h1>Hello,!!!</h1>'

@app.route('/insert')
def insert():
    admin_role = Role(name='Admin')
    user_john = User(username='john')

   # db.session.add(admin_role)
   # db.session.add(user_john)

   # db.session.commit()
    i = User.query.filter_by(id=1)
    for j in i:
        print(j)
    # print(admin_role.id)
    return render_template('index.html')

@app.route('/sreach')
def sreach():
    cursor = db.cursor()

    sql = "INSERT INTO roles(name) VALUES ('Anne')"
    cursor.execute(sql)
    db.commit()
    print('OK', cursor.rowcount)
    return 'OK'

if __name__ == '__main__':
    app.run()
