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
    unit_id = db.Column(db.BigInteger)


class Manager(db.Model):
    """
    项目负责人
    """
    __tablename__ = 'manager'
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(25))
    unit = db.Column(db.String(25))
    position = db.Column(db.String(25))
    gender = db.Column(db.SmallInteger)
    nationality = db.Column(db.String(20))
    birthday = db.Column(db.String(20))
    expertise = db.Column(db.String(20))
    tutor = db.Column(db.String(10))
    system = db.Column(db.String(10))


class Unit(db.Model):
    """
    依托单位
    """
    __tablename__ = 'unit'
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(25))
    phone = db.Column(db.String(30))
    post = db.Column(db.String(20))
    location = db.Column(db.String(30))


class Member_info(db.Model):
    __tablename__ = 'member_info'
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(20))
    gender = db.Column(db.String(10))
    birthday = db.Column(db.String(20))


class Member2pro(db.Model):
    __tablename__ = 'member2pro'
    id = db.Column(db.BigInteger, primary_key=True)
    mid = db.Column(db.BigInteger)
    pid = db.Column(db.BigInteger)

# class Expected_Performance(db.Model):
#     """
#     项目预期成果
#     """
#     __tablename__ = 'expected_performance'
#     id = db.Column(db.BigInteger, primary_key=True)
#     content = db.Column(db.Text)
#     expenses = db.Column(db.BigInteger)
#     deadline = db.Column(db.DateTime)
