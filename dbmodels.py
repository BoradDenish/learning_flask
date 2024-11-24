from dbapp import db

class Person(db.Model):
    __tablename__ = 'people'

    pid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer)
    job = db.Column(db.String(100))

    def __repr__(self):
        return f'Person(name={self.name}, age={self.age}, job={self.job})'
