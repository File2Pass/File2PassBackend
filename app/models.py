from . import db


class Project(db.Model):
    """
    项目信息
    """
    __tablename__ = 'project'
    id = db.Column(db.BigInteger, primary_key=True)
    type = db.Column(db.String(25))
    summary = db.Column(db.Text)
    name = db.Column(db.String(25))
    manager_id = db.Column(db.BigInteger)
    uint_id = db.Column(db.BigInteger)
    expected_performance_id = db.Column(db.BigInteger)
    content = db.Column(db.Text)


class Manager(db.Model):
    """
    项目负责人
    """
    __tablename__ = 'manager'
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(25))
    uint = db.Column(db.String(25))
    postion = db.Column(db.String(25))
    sex = db.Column(db.SmallInteger)


class Unit(db.Model):
    """
    依托单位
    """
    __tablename__ = 'uint'
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(25))
    location = db.Column(db.String(30))


class Expected_Performance(db.Model):
    """
    项目预期成果
    """
    __tablename__ = 'expected_performance'
    id = db.Column(db.BigInteger, primary_key=True)
    content = db.Column(db.Text)
    expenses = db.Column(db.Double)
    deadline = db.Column(db.DateTime)
