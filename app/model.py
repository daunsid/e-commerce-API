#from email.policy import default
#from email.policy import default
from .database import  Base
from sqlalchemy_utils import URLType
from slugify import slugify
from sqlalchemy import DECIMAL, DateTime, Column, Integer, String, Boolean, TEXT
from datetime import datetime



class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    slug = Column(String, unique=True)
    url = Column(URLType)
    description = Column(TEXT)
    price = Column(DECIMAL(scale=2))
    available = Column(Boolean, default=True)
    created_date = Column(DateTime, default=datetime.utcnow)
    updated = Column(DateTime, onupdate = datetime.now)

    
    def __init__(self, *args, **kwargs):
        if not 'slug' in kwargs:
            kwargs['slug'] = slugify(kwargs.get('title', ''))
        super().__init__(*args, **kwargs)
    
