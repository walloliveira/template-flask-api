from database import db

_session = db.session


def save(model: db.Model):
    _session.add(model)
    commit()
    return model


def commit():
    _session.commit()

