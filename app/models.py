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
