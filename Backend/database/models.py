from database import db

class Person(db.Model):
    __tablename__ = 'person'
    pid = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(120)) 
    password = db.Column(db.String(60))
    iban = db.Column(db.String(34))
    bic = db.Column(db.String(12))
    transactions = db.relationship('Transaction', backref='creditor', lazy='dynamic')
    assets = db.relationship('Asset', backref='debitor', lazy='dynamic')

    def __repr__(self):
        return '<User %r>' % (self.nickname)

    def __init__(self, firstname, lastname, username, email="", pwd="", iban="", bic=""):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.email = email
        self.password = pwd
        self.iban = iban
        self.bic = bic


class Transaction(db.Model):
    __tablename__ = 'transaction'
    tid = db.Column(db.Integer, primary_key=True)
    creditor_id = db.Column(db.Integer, db.ForeignKey('person.pid'), nullable=False)
    shop_id = db.Column(db.Integer, db.ForeignKey('shop.sid'), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    attachment = db.Column(db.LargeBinary)
    comment = db.Column(db.String(150))


class Asset(db.Model):
    __tablename__ = 'asset'
    aid = db.Column(db.Integer, primary_key=True)
    trans_id = db.Column(db.Integer, db.ForeignKey('transaction.tid'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    debitor_id = db.Column(db.Integer, db.ForeignKey('person.pid'))
    comment = db.Column(db.String(150))
    tag = db.Column(db.String(150))


class Shop(db.Model):
    __tablename__ = 'shop'
    sid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200))
    zip = db.Column(db.String(12))
    transactions = db.relationship('Transaction', backref='shop', lazy='dynamic')

