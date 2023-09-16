# models.py

from datetime import datetime
from config import db, ma


class User(db.Model):
    __tablename__ = "user"
    uid = db.Column(db.String(32), primary_key=True)
    bech32 = db.Column(db.String(32), unique=True)
    herotag = db.Column(db.String(32))
    creation_timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    log_timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        sqla_session = db.session


user_schema = UserSchema()
people_schema = UserSchema(many=True)
