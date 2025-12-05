from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///farm.db"

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

def init_db():
    from models.animal import Animal
    from models.category import Category
    from models.feed import Feed
    from models.product import Product

    Base.metadata.create_all(bind=engine)
