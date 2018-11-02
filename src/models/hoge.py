from datetime import datetime

from flask_marshmallow import Marshmallow

from flask_marshmallow.fields import fields

from sqlalchemy_utils import UUIDType

from src.database import db

import uuid

ma = Marshmallow()

from .parent import ParentModel, ParentSchema


class HogeModel(db.Model):
  __tablename__ = 'hoges'

  id = db.Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
  name = db.Column(db.String(255), nullable=False)
  state = db.Column(db.String(255), nullable=False)
  parent_id = db.Column(UUIDType(binary=False), db.ForeignKey('parents.id'), nullable=False)
  parent = db.relationship("ParentModel", backref='hoges')

  createTime = db.Column(db.DateTime, nullable=False, default=datetime.now)
  updateTime = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

  def __init__(self, name, state, parent_id):
    self.name = name
    self.state = state
    self.parent_id = parent_id


  def __repr__(self):
    return '<HogeModel {}:{}>'.format(self.id, self.name)


class HogeSchema(ma.ModelSchema):
  class Meta:
    model = HogeModel

  createTime = fields.DateTime('%Y-%m-%dT%H:%M:%S')
  updateTime = fields.DateTime('%Y-%m-%dT%H:%M:%S')
  parent = ma.Nested(ParentSchema)
