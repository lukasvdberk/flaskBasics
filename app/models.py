from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Post(Base):
    __tablename__ = 'Post'

    id = Column(Integer, primary_key=True)
    title = Column(String(50), unique=True)
    post_content = Column(String(2000000000))

    def __init__(self, title, post_content):
        self.title = title
        self.post_content = post_content

    def __repr__(self):
        return self.title