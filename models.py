from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,Float,text


Base = declarative_base()

class Blog(Base):
    __tablename__ = 'blog'

    id = Column(Integer, primary_key=True)
    name = Column(String(60), nullable=False, server_default=text(''))
    price = Column(Float, nullable=False,server_default = text('0'))
    author = Column(String(64), server_default=text(''))
