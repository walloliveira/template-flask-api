from database import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(120))

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
        }
