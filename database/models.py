# -*- coding: utf-8 -*-
from sqlalchemy import Column, String, SMALLINT, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mysql import TIMESTAMP
from datetime import datetime

DB_SETTING = {
    'drivername': 'mysql+mysqlconnector',
    'host': '127.0.0.1',
    'port': '3306',
    'database': 'Mail',
    'username': 'root',
    'password': '',
    'query': {
        'charset': 'utf8'
    }
}

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8'
    }

    uid = Column(String(100))
    mail = Column(String(255), nullable=False, primary_key=True)
    name = Column(String(50))
    white = Column(SMALLINT, default=1, doc=u"若用户退订，则白名单置为0")
    status = Column(SMALLINT, default=1, doc=u"表示最后一次发送是否成功")
    send_times = Column(Integer, default=0, doc=u"向用户发送邮件总次数")
    add_time = Column(TIMESTAMP, nullable=False, default=str(datetime.now()))
    last_time = Column(TIMESTAMP)

class AmazonUser(Base):
    __tablename__ = 'amazon_user'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8'
    }


    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(20), nullable=False)
    password = Column(String(500), nullable=False)
    level = Column(Integer, nullable=False)


class InternalMail(Base):
    __tablename__ = 'internal_mail'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8'
    }


    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    order_time = Column(TIMESTAMP, nullable=False, default=str(datetime.now()))
    shipment_id = Column(String(50), nullable=False)
    other = Column(String(50))



class ExternalMail(Base):
    __tablename__ = 'external_mail'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8'
    }


    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    shipment_id = Column(String(50), nullable=False)
    test = Column(String(50))
    white = Column(SMALLINT, default=1)


class OtherMail(Base):
    __tablename__ = 'other_mail'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8'
    }


    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    mail = Column(String(50), nullable=False)
    name = Column(String(50))
    white = Column(SMALLINT, default=1)
    status = Column(SMALLINT, default=1)