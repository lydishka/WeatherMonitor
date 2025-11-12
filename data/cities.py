import sqlalchemy

from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase


class Cities(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'cities'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True,
                           autoincrement=True)
    city_name = sqlalchemy.Column(sqlalchemy.String)