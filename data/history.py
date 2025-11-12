import sqlalchemy

from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase


class History(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'history'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True,
                           autoincrement=True)
    city_name = sqlalchemy.Column(sqlalchemy.String)
    city_temp = sqlalchemy.Column(sqlalchemy.Float)
    city_humidity = sqlalchemy.Column(sqlalchemy.Float)
    city_pressure = sqlalchemy.Column(sqlalchemy.Float)
    city_wind_speed = sqlalchemy.Column(sqlalchemy.String)
    city_weather_desc = sqlalchemy.Column(sqlalchemy.String)
    city_weather_data = sqlalchemy.Column(sqlalchemy.String)