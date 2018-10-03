import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class ics_shares_upload(Base):
    __tablename__ = 'ics_shares_upload'

    client_prefix = Column(Integer, primary_key=True)
    client_suffix = Column(String(250), nullable=False)
    joint_acct_no = Column(Integer, nullable=False)
    member_prefix = Column(String(10), nullable=False)
    member_prefix = Column(String(10), nullable=False)
    total_subscribed_shares = Column(Integer, nullable=False)

class csd_shares_upload(Base):
    __tablename__ = 'csd_shares_upload'

    client_prefix = Column(Integer, primary_key=True)
    client_suffix = Column(String(250), nullable=False)
    joint_acct_no = Column(Integer, nullable=False)
    member_prefix = Column(String(10), nullable=False)
    member_prefix = Column(String(10), nullable=False)
    total_subscribed_shares = Column(Integer, nullable=False)


engine = create_engine('sqlite:///sharesUpload.db')
Base.metadata.create_all(engine)
print('db created!')