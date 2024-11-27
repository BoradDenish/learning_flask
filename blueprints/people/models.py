from blueprints.blueprintapp import db

class People(db.Model):
    __tablename__ = 'peoples'

    pid     = db.Column(db.Integer, primary_key=True)
    name    = db.Column(db.String, nullable=False)
    age     = db.Column(db.Integer)
    job     = db.Column(db.String)

    def __repr__(self):
        return f"<People {self.name}, Age: {self.age}"
    
    def get_id(self):
        return self.pid