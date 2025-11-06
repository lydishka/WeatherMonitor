import sqlalchemy

from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase


class Cities(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'cities'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True,
                           autoincrement=True)
    city_nane = sqlalchemy.Column(sqlalchemy.String)
    city_owner = sqlalchemy.Column(sqlalchemy.Integer)