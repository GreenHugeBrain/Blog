from ext import db, app, login_manager
from flask_login import UserMixin

class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String)
  surname = db.Column(db.String)
  email = db.Column(db.String)
  password = db.Column(db.String)

@login_manager.user_loader
def load_user(user_id):
   return User.query.get(user_id)


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    text = db.Column(db.String, nullable=False)
    img = db.Column(db.String, nullable=True)
    author_id = db.Column(db.ForeignKey("user.id"))
    author = db.relationship("User")


if __name__ == '__main__':
  with app.app_context():
    db.create_all()